WORDS = [u"KONGTIAO"]
SLUG = "airconditioner"
PRIORITY = 8
_trigger_words = [u'空调', u'冷', u'热']


def handle(text):
	res = {
	"service": "airconditioner"
	}
	slot = {}
	if (u"打开" in text) or (u"开" in text):
		slot['attr'] = "power"
		slot['attrType'] = "String"
		slot['attrValue'] = "on"
	elif (u"关掉" in text) or (u"关" in text):
		slot['attr'] = "power"
		slot['attrType'] = "String"
		slot['attrValue'] = "on"
	elif (u"太热" in text) or (u"真热" in text) or (u"好热" in text):
		slot["attr"] = "temperature"
		slot["attrType"] = "Object(digital)"
		slot["attrValue"] = {
							"direct": "-"
							}
	elif (u"太冷" in text) or (u"真冷" in text) or (u"好冷" in text):
		slot["attr"] = "temperature"
		slot["attrType"] = "Object(digital)"
		slot["attrValue"] = {
							"direct": "+"
							}
	res['slot'] = slot
	return res

def isValid(text):
	return any(word in text for word in _trigger_words)

if __name__ == "__main__":
	print(handle(u"太热了"))