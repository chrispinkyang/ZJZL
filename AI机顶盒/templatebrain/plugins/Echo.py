# -*- coding: utf-8-*-

WORDS = [u"ECHO", u"CHUANHUA"]
SLUG = "echo"
PRIORITY = 0

_trigger_words = ["echo", u"传话"]


def handle(text):
    res = {}
    return {'slot': res}


def isValid(text):
    return any(word in text.lower() for word in _trigger_words)
