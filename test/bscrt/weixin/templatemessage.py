import logging
import requests
import os
import json

def get_access_token():
    appid = 'wx6bcc04938546d3b7'
    secret = '6361eaf79e717e13cb5c7df4dc2c9a93'
    req_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid, secret)
    r = requests.get(req_url,)
    if r.status_code==200:
        rjson=r.json()
        if 'access_token' in rjson:
            return (1,rjson['access_token'])
        else:
            return (0,rjson['errmsg'])
    else:
        return (0,"request error")

def send_template_message(openid, template_id, form_id, data, page, emphasis_keyword=None):
    status, access_token = get_access_token()
    req_url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}".format(access_token)
    if emphasis_keyword:
        payload = {
            "touser": openid,
            "template_id": template_id,
            "page": page,
            "form_id": form_id,
            "data": data,
            "emphasis_keyword": emphasis_keyword
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
        r = requests.post(req_url, json=payload)
        if r.status_code == 200:
            rjson = r.json()
            errcode = rjson['errcode']
            logging.debug(errcode)
            if errcode == 0:
                logging.debug("send template message success")
            else:
                logging.error("{}:{}".format(errcode, rjson['errmsg']))
        else:
            logging.debug("other error")
    except Exception as e:
        logging.exception(e)


def answers_notification(answers_id, answers_count):
    try:
        logging.debug("answers_notification")
        openid = "oISwc5O4M_mh7Hwjfrur9QsfTBaA"
        print("openid in answers_notification", openid)
        # 模版消息:提问回复通知
        template_id = "rYPaEliit5SnfftqsIfl-oR2Sz671gtaa4wjMiqXvI4"
        # form_ids
        form_id = "0d3ad3463058b2b306d29e15642fdc87"
        data = {
            "keyword1":
                {"value": "test"},
            "keyword2":
                {"value": "answers_count"},
            "keyword3":
                {"value": "answer.user.nickname"},
            "keyword4":
                {"value": "answer.content"}
        }
        # page = "pages/myClockRecord/myClockRecord?id=" + str(question.id)
        # 开发版模板消息推送
        page = "pages/index/index"
        send_template_message(openid, template_id, form_id, data, page)
    except Exception as e:
        logging.error(e.args)


answers_notification(1,1)

with transaction.atomic():
    ins = Snippet.objects.get(pk=2)
    ins.code += 'monday'
    ins.save()
    async_test.delay()