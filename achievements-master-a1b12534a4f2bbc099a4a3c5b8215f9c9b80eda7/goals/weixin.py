import time,os
import json
try:
    from xml.etree import cElementTree as ETree
except ImportError:
    from xml.etree import ElementTree as ETree
#from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
import random
import string
import hashlib
import requests
import logging
import datetime
import pytz
import io

from django.utils import timezone
from django.core.cache import cache
from django.conf import settings
from django.db.models import Sum

from goals.models import Wallet,TransactionRecord

def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''

    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


def xml_to_dict(content):
    raw = {}
    root = ETree.fromstring(content)
    for child in root:
        raw[child.tag] = child.text
    return raw


def request_with_cert(url, param, headers):
    cert = (settings.WEIXIN_CERT_PATH, settings.WEIXIN_KEY_PATH)
    print(cert)
    r = requests.post(url, data=param, headers=headers, cert=cert)
    return r


def generate_nonce_str():
    ascii_letters = string.ascii_letters
    digits = string.digits
    letters = ascii_letters + digits
    nonce_str = ''.join([random.choice(letters) for i in range(32)])
    # self.param.update({"nonce_str":nonce_str})
    return nonce_str


def generate_sign(param, sec_key, sign_type):
    # nonce_str=generate_nonce_str()
    # self.param['nonce_str']=nonce_str
    if sign_type == 'MD5':
        sign_type = 'md5'
    elif sign_type == 'HMAC-SHA256':
        sign_type = "sha256"
    else:
        raise TypeError("sign-type not support {},it must be one of the [md5,sha256]".format(sign_type))
    param = {k: v for k, v in param.items() if v is not None}
    sorted_keys = sorted(param)
    stringA = "&".join(["{}={}".format(key, param[key]) for key in sorted_keys])
    stringA = "&".join([stringA, "key={}".format(sec_key)])
    print("stringA:{}".format(stringA))
    m = getattr(hashlib, sign_type)()
    m.update(stringA.encode('utf8'))
    print("m:{}".format(m))
    sign = m.hexdigest().upper()
    print("sign:{}".format(sign))
    # param.update({"sign":sign})
    return sign


class WeixinPay(object):
    def __init__(self, appid, mch_id, key, notify_url, trade_type="JSAPI", device_info=None, sign_type="MD5"):
        self.appid = appid
        self.mch_id = mch_id
        self.key = key
        self.notify_url = notify_url
        self.trade_type = trade_type
        self.device_info = device_info
        self.sign_type = sign_type

    def generate_pay_info(self, openid, desc, amount, check_name='NO_CHECK', re_user_name=None):
        if not isinstance(amount, int):
            raise TypeError("amount needs to be a int")
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        print("timestamp:{}".format(timestamp))
        hexdigits = string.hexdigits
        print("hexdigits:{}".format(hexdigits))
        partner_trade_no = "GOAL" + ''.join(random.sample(hexdigits, 4)) + timestamp
        print("partner_trade_no:{}".format(partner_trade_no))
        spbill_create_ip = "127.0.0.1"
        order_info = {
            "openid": openid,
            "desc": desc,
            "amount": amount,
            "check_name": check_name,
            "re_user_name": re_user_name,
            "spbill_create_ip": spbill_create_ip,
            "partner_trade_no": partner_trade_no
        }
        return order_info

    def generate_order_info(self, openid, body, total_fee, detail=None, attach=None, fee_type="CNY"):
        if not isinstance(total_fee, int):
            raise TypeError("total_fee needs to be a int")
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        hexdigits = string.hexdigits
        out_trade_no = "GOAL" + ''.join(random.sample(hexdigits, 4)) + timestamp
        spbill_create_ip = "127.0.0.1"
        order_info = {
            "openid": openid,
            "body": body,
            "total_fee": total_fee,
            "detail": detail,
            "attach": attach,
            "fee_type": fee_type,
            "spbill_create_ip": spbill_create_ip,
            "out_trade_no": out_trade_no
        }
        # self.param.update(order_info)
        return order_info

    def generate_refund_info(self, **data):
        if not {"transaction_id", "out_trade_no"} & data.keys():
            raise ValueError("one of (transaction_id,out_trade_no) must be provide")
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        print("timestamp:{}".format(timestamp))
        hexdigits = string.hexdigits
        print("hexdigits:{}".format(hexdigits))
        out_refund_no = "GOAL" + ''.join(random.sample(hexdigits, 4)) + timestamp
        data.update({"out_refund_no": out_refund_no})
        return data

    def generate_orderquery_info(self, **data):
        if not {"transaction_id", "out_trade_no"} & data.keys():
            raise ValueError("one of (transaction_id,out_trade_no) must be provide")
        return data

    def generate_nonce_str(self):
        nonce_str = generate_nonce_str()
        # self.param['nonce_str']=nonce_str
        return nonce_str

    def generate_sign(self, param, key):
        sign = generate_sign(param, key, self.sign_type)
        return sign

    def make_request(self, url, param, user_cert=False):
        request_param = tostring(dict_to_xml('xml', param))
        print("request_param:{}".format(request_param))
        headers = {"Content-Type": "application/xml"}
        if not user_cert:
            r = requests.post(url, data=request_param, headers=headers)
        else:
            r = request_with_cert(url, request_param, headers=headers)
        if r.status_code == 200:
            content = r.content
            dict_content = xml_to_dict(content)
            tree = ETree.fromstring(r.content)
            print(dict_content)
            return tree
        else:
            return None


def get_access_token():
    appid=settings.WEIXIN_APPID
    secret=settings.WEIXIN_SECRET
    req_url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid,secret)
    r=requests.get(req_url,)
    if r.status_code==200:
        rjson=r.json()
        if 'access_token' in rjson:
            return (1,rjson['access_token'])
        else:
            return (0,rjson['errmsg'])
    else:
        return (0,"request error")


def send_template_message(openid,template_id,form_id,data,page,emphasis_keyword=None):
    access_token=cache.get('token')
    if access_token is None:
        logging.info("get access_token")
        status,access_token=get_access_token()
        if status:
            cache.set('token',access_token)
        else:
            raise RuntimeError("get access token failure")
    req_url="https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}".format(access_token)
    if emphasis_keyword:
        payload={
        "touser":openid,
        "template_id":template_id,
        "page":page,
        "form_id":form_id,
        "data":data,
        "emphasis_keyword":emphasis_keyword
        }
    else:
        payload = {
            "touser": openid,
            "template_id": template_id,
            "page": page,
            "form_id": form_id,
            "data": data,
        }
    try:
        logging.debug(payload)
        print(payload)
        r=requests.post(req_url,json=payload)
        if r.status_code==200:
            rjson=r.json()
            errcode=rjson['errcode']
            logging.debug(errcode)
            if errcode==0:
                logging.debug("send template message success")
            else:
                logging.error("{}:{}".format(errcode,rjson['errmsg']))
        else:
            logging.debug("other error")
    except Exception as e:
        logging.exception(e)


def generate_qrcode(username,goal_id):
    logging.info("generate qrcode")
    access_token = cache.get('token')
    if access_token is None:
        logging.info("get access_token")
        status, access_token = get_access_token()
        if status:
            cache.set('token', access_token)
        else:
            raise RuntimeError("get access token failure")
    req_url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit"
    scene="?id={}".format(goal_id)
    data = {
            "scene": scene,
            "page": "pages/confirmTarget/confirmTarget",
            "width": 250,
            "is_hyaline": True
    }

    querystring = {"access_token": access_token}

    headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
        }

    response = requests.request("POST", req_url, data=json.dumps(data), headers=headers, params=querystring,stream=True)

    if response.status_code == 200:
        filename="_".join(["qrcode",username,str(goal_id)])+'.jpeg'
        filepath = os.path.join(settings.BASE_DIR, 'media/qrcode',filename)
        #imgBuf=io.BytesIO(response.content)
        #img=Image.open(imgBuf)
        #img=img.resize((106,106),Image.ANTIALIAS)
        #img.save(filepath)
        with open(filepath,'wb') as f:
            for chunk in response.iter_content(512):
                f.write(chunk)
        return os.path.join("qrcode",filename)

def banlance_validate(user):
    wallet=Wallet.objects.get(user=user)
    banlance=wallet.banlance
    records=TransactionRecord.objects.aggregate(banlance=Sum('amount'))
    if banlance!=records['banlance']:
        return False
    else:
        return True

