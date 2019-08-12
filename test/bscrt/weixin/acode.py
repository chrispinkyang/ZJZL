import requests
import os
import json

# zhiliaojun
# WEIXIN_APPID = 'wxa99093dfc554a99f'
# WEIXIN_SECRET = '7ab0db367536aab85562a56f918029e7'

# putongyundong
WEIXIN_APPID = 'wx5cda917f15615ce7'
WEIXIN_SECRET = '6d0b5608a684da15c3e0ad623b2a679e'

def get_access_token():
    appid = WEIXIN_APPID
    secret = WEIXIN_SECRET
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

def generate_qrcode(username, question_id):
    print("generate qrcode")
    print("get access_token")
    status, access_token = get_access_token()
    if status:
        print("get access token success")
    else:
        raise RuntimeError("get access token failure")
    req_url = "https://api.weixin.qq.com/wxa/getwxacode"
    scene = "?id={}".format(question_id)
    data = {
        # 发布之前, page为空
        "path": "pages/activity/poster/poster",
        #"auto_color":False,
        # "line_color": {"r": "185", "g": "185", "b": "185"},
        "width": 250,
        "is_hyaline": True
    }

    querystring = {"access_token": access_token}

    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", req_url, data=json.dumps(data), headers=headers, params=querystring,
                                stream=True)

    try:
        print(response.json())
    except:
        print(type(response.content))
        if response.status_code == 200:
            filename = "_".join(["qrcode", username, str(question_id)]) + '.jpeg'
            filepath = os.path.join('C:/Users/52489/Desktop/ZJZL/test/bscrt/weixin', filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(512):
                    f.write(chunk)
            return os.path.join("qrcode", filename)
            print("success")


# print(get_access_token())
generate_qrcode("chrispink",1)