class AbstractPlugin(object):
	"""docstring for AbstractPlugin"""
	__trigger_words = []

	def handle(self, text):
		print("handle method must be implemented")

	def is_valid(self):
		return any(word in text for word in __trigger_words)