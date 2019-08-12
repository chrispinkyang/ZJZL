# -*- coding: utf-8-*-

import os
import shutil

WORDS = [u"HUANCUN"]
SLUG = "cleancache"
PRIORITY = 0

_trigger_words = ["清除缓存", u"清空缓存", u"清缓存"]

def handle(text):
    res = {}
    return {'slot':res}

def isValid(text):
    return any(word in text.lower() for word in _trigger_words)
