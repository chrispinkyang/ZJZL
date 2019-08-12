import requests

WORDS = ["KONGTIAO"]
SLUG = "airconditioner"
_trigger_words = [u'聊聊',u'聊天',u'谈谈']


def handle(text):
	res = {
	"service": "Turing"
	}
	slot = {}
	data = {"reqType":0,
	"perception": {
		"inputText": {
			"text": text
		},
		"inputImage": {
			"url": "imageUrl"
			},
		"selfInfo": {
		"location": {
			"city": "北京",
			"province": "北京",
			"street": "信息路"
			}
		}
	},
	"userInfo": {
		"apiKey": "db22788e41ae4eb79445fb4a5e61c4ac",
		"userId": "317370"
		}
	}

	url = "http://openapi.tuling123.com/openapi/api/v2"

	resp = requests.post(url, json=data)
	if resp.status_code == 200:
		resp_text = resp.json()['results'][0].get('values').get('text')
		slot['attr'] = 'text'
		slot['attrType'] = 'String'
		slot['attrValue'] = resp_text
	res['slot'] = slot
	return res

def isValid(text):
	return any(word in text for word in _trigger_words)

if __name__ == "__main__":
	print(handle(u"太热了"))