import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

class ParsingText(object):
    LTP_DATA_DIR = 'D:\\Ddesktop\\Python\\ltp_model\\3.4'

    def __init__(self, text):
        self._text = text
        self._words = []  # 分词结果 generator
        self._postags = []  # 词性标注 generator
        self._netags = []  # 命名实体识别 generator
        from collections import defaultdict
        self._category = defaultdict(list)  # 词分类

    def get_text(self):
        return self._text

    def parse_words(self):
        # To-do: redis set modelfile.name modelfle
        # 分词
        cws_model_path = os.path.join(self.LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        segmentor = Segmentor()  # 初始化实例
        segmentor.load(cws_model_path)  # 加载模型
        words = segmentor.segment(self._text)  # 分词
        print('分词:')
        print('\t'.join(words))
        self._words = words
        segmentor.release()
        
    def parse_postags(self):
        #词性标注
        if not self._words:
            self.parse_words()
        pos_model_path = os.path.join(self.LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        postagger = Postagger() # 初始化实例
        postagger.load(pos_model_path)  # 加载模型
        postags = postagger.postag(self._words)  # 词性标注
        print('词性标注:')
        print('\t'.join(postags))
        self._postags = postags
        postagger.release()
    
    def parse_netags(self):
        # 命名实体识别
        if not self._postags:
            self.parse_postags()
        ner_model_path = os.path.join(self.LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`ner.model`
        recognizer = NamedEntityRecognizer() # 初始化实例
        recognizer.load(ner_model_path)  # 加载模型
        netags = recognizer.recognize(self._words, self._postags)  # 命名实体识别
        print('命名实体识别:')
        print('\t'.join(netags))
        self._netags = netags
        recognizer.release()
    
    def generate_category(self):
        if not self._netags:
            self.parse_netags()
        category = self._category
        words, postags, netags = self.get_words(), self.get_postags(), self.get_netags()
        for word, postag,netag in zip(words, postags, netags):
            category[postag].append(word)
            category[netag].append(word)

    def get_words(self):
        if not self._words:
            self.parse_words()
        return list(self._words)

    def get_postags(self):
        if not self._postags:
            self.parse_postags()
        return list(self._postags)

    def get_netags(self):
        if not self._netags:
            self.parse_netags()
        return list(self._netags)

    def get_location(self):
        if not self._category:
            self.generate_category()
        return self._category['ns']

    def get_name(self):
        if not self._category:
            self.generate_category()
        return self._category['nh']

    def get_time(self):
        if not self._category:
            self.generate_category()
        return self._category['nt']

    def get_noun(self):
        if not self._category:
            self.generate_category()
        return self._category['n']


if __name__ == "__main__":
    test = u"今天广州的天气怎么样"
    p = ParsingText(test)
    print(p.get_words())
    print(p.get_postags())
    print(p.get_netags())
    print(p.get_location())
    print(p.get_time())
