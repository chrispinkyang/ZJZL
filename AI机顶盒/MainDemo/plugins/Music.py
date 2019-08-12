WORDS = [u"YINYUE"]
SLUG = "music"
PRIORITY = 7
_trigger_words = [u'音乐', u'歌曲', u'歌']

def handle(pt):
	# exract keywords
	exclude_words = {'请','播放','一首',}
	words = pt.get_words()

	from plugins.utils.QQMusic import QQMusic
	qqmusic = QQMusic()
	
	song_list = qqmusic.search_song(pt.get_text())
	print('song_list:', song_list)
	sng = song_list[0]
	print('return_url:')
	print(sng.get_music_url())
	
def isValid(text):
	return any(word in text.lower() for word in _trigger_words)

if __name__ == "__main__":
	test = u"三人游"
	from ParsingText import ParsingText
	pt = ParsingText(test)
	handle(pt)
