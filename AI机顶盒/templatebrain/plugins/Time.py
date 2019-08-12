# -*- coding: utf-8-*-
import datetime
from pytz import timezone
# from semantic.dates import DateService

WORDS = [u"TIME", u"SHIJIAN", u"JIDIAN"]
SLUG = "time"

_trigger_words = [u"时间", u"几点"]

def handle(text):
    res = {}
    return {'slot':res}

def isValid(text):
    return any(word in text for word in _trigger_words)
