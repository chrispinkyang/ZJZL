from hashlib import md5

import requests
from datetime import datetime
openid = 'JH1257c5ded253ba1ba879147372437563'
key = '2f6051d5f6eb807cfb82eb6d7da9ac08'
phoneno = '18819451571'
cardnum = '1'
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
orderid = timestamp + phoneno + cardnum
#orderid = '26536256425'
print(orderid)
url = 'http://op.juhe.cn/ofpay/mobile/onlineorder'
md5 = md5()
md5.update((openid+key+phoneno+cardnum+orderid).encode('utf-8'))
# 校验值，md5(OpenID+key+phoneno+cardnum+orderid)，OpenID在个人中心查询
sign = md5.hexdigest()
# phoneno=18819451571&cardnum=1&orderid=11111111&sign=eaac475a9fe89bf96e002b4d6e0cb025&key=2f6051d5f6eb807cfb82eb6d7da9ac08
data = {
	'phoneno': phoneno,
	'cardnum':cardnum,
	'orderid':orderid,
	'sign':sign,
	'key':key
}
res = requests.post(url, data=data)
res_json = res.json()
print(res_json['error_code'])
print(res_json['reason'])