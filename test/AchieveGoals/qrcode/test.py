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


goal_id = 20
username = 'oAUG94qYKfRFs6WZLZUFkChTnQN8'
req_url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit"
data = {'scene': '?id=20', 'page': 'pages/index/index', 'width': 250, 'is_hyaline': True}
headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
status, access_token = get_access_token()
#access_token = '12_Ug1Gg7jFs8PybCMKDzyqd2Af4wJIlgL05kMWtJBnVwuWreCvHvkOGyH0gMjmluhoRuGrgwhff98i7MxgwaCiOaI_SJ8W4cTDp_YOgxf5iq55r2UZqMoY16rrxx6WfCJtcJCiSeEP1KmA2U7eLMYcAHAWXJ'
print(access_token)
querystring = {'access_token': access_token}
response = requests.request("POST", req_url, data=json.dumps(data), headers=headers, params=querystring,stream=True)
print(response)
# print(response.json())
if response.status_code == 200:
	filename="_".join(["qrcode",username,str(goal_id)])+'.jpeg'
	filepath = os.path.join('C:\\Users\\52489\\Desktop\\Python\\qrcode', filename)
	with open(filepath,'wb') as f:
		for chunk in response.iter_content(512):
			f.write(chunk)
			print("write successfully")
		print(os.path.join("qrcode",filename))