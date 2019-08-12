# -*- coding: utf-8-*-
from __future__ import absolute_import
import logging
import plugin_loader
from ParsingText import ParsingText


class Brain(object):

    def __init__(self):

        self.plugins = plugin_loader.get_plugins()
        print("plugins in Brain:", self.plugins)
        self._logger = logging.getLogger(__name__)
        self.handling = False

    def query(self, text):
        '''
        texts: a list with sentence.
        '''
        for plugin in self.plugins:
            if not plugin.isValid(text):
                continue

            self._logger.debug("'%s' is a valid phrase for plugin " +"'%s'", text, plugin.__name__)
            # continueHandle = False
            # 以缓存实现上下文
            try:
                self.handling = True
                print("before handling")
                pt = ParsingText(text)
                res = plugin.handle(pt)
                print("after handling")
                self.handling = False
            except Exception:
                print('Failed to execute plugin')
                self._logger.error('Failed to execute plugin', exc_info=True)
            else:
                print("Handling of phrase '%s' by " +"plugin '%s' completed", text, plugin.__name__)
                self._logger.debug("Handling of phrase '%s' by " +"plugin '%s' completed", text,plugin.__name__)
            finally:
                print(res)
                return res
        self._logger.debug("No plugin was able to handle any of these " + "phrases: %r", text)
        print("No plugin was able to handle any of these "+ "phrases:" + text)

if __name__ == "__main__":
    b = Brain()
    res = b.query(u'广州今天天气怎么样')
    print(type(res))