import requests
import json
import os



def get_access_token():
    #appid = 'wxed0b5e2f6f2b7361'
    appid = 'wx5cda917f15615ce7'
    #secret = '5c0b1ba0dd2b57cd3d81dac2932d1b22'
    secret = '6d0b5608a684da15c3e0ad623b2a679e'
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
    print("get access_token")
    status,access_token=get_access_token()
    req_url="https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}".format(access_token)
    payload = {
    "touser": openid,
    "template_id": template_id,
    "page": page,
    "form_id": form_id,
    "data": data,
        }
    r=requests.post(req_url,json=payload)
    if r.status_code==200:
        print(rjson=r.json())
    else:
        print("other error")


if __name__ == '__main__':
    print("supervise notification")
openid = "goAUG94lCaXW7J9Jr09wMXQkFXMxo"
template_id = "dhOXhgPWFLXqep2ioM9EFtt1qVuwgk9eUIz9eWr71z0"
data = {
    "keyword1":
        {"value": "test_content"},
    "keyword2":
        {"value": "test_nickname"},
    "keyword3":
        {"value": "test_DateTime"}
}
# page="/pages/singleClock/singleClock?="+str(goal.id)
page = "/pages/index/index"
send_template_message(openid, template_id, form_id, data, page)
