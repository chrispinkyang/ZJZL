class BaseConvertor(object):
	"""docstring for BaseConvertor"""
	pass

class WeatherConvertor(BaseConvertor):
	def __init__(self, json_data):
		# initial by a json_data: response[0]
		self.json_data = json_data

	def get_result(self):
		json_data = self.json_data
		intent = json_data['intent']
		res = {
		'SpeechTexts': intent['answer']['text'],
		'Service': 'weather',
		'intent': 'query'
		}
		result_list = intent['data']['result']
		data = []
		for result in result_list:
			each = dict()
			each = {
			"city": result['city'],
			"date": result['date'],
			"date_for_voice": ['date_for_voice'],#"今天"/"明天"/"后天"/x号
			"img": result['img'],#气象图url
			"lastUpdateTime": result['lastUpdateTime'],
			"tempHigh": result['tempHigh'],
			"tempLow": result['tempLow'],
			"tempRange": result['tempRange'],
			"weather": result['weather'],
			"weatherDescription": result['weatherDescription'],
			"weatherType": result['weatherType'],
			"week": result['week'],
			"wind": result['wind'],
			"windLevel": result['windLevel']
			}
			data.append(each)
		res['data'] = data
		return res