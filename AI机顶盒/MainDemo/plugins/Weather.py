from plugins.utils.Webaiui import request2Aiui
from plugins.utils.Convertors import WeatherConvertor

WORDS = [u"TIANQI"]
SLUG = "weather"
PRIORITY = 6
_trigger_words = [u'天气']


def handle(pt):
	text = pt.get_text()
	json_res = request2Aiui(text)
	convertor = WeatherConvertor(json_res)
	res = convertor.get_result()
	return res

def isValid(text):
	return any(word in text.lower() for word in _trigger_words)

if __name__ == "__main__":
	from ParsingText import ParsingText
	from utils.Webaiui import request2Aiui
	from utils.Convertors import WeatherConvertor
	text = u"今天广州天气怎么样"
	pt = ParsingText(text)
	print(isValid(text))
	print(handle(pt))