# -*- coding: utf-8-*-
import random

WORDS = []

trigger_words = []

replies = [
u'是不是刚才我走神了，主人能再说一次吗',
u'看来我被难倒了，没有明白主人的意思',
u'找不到主人要的内容，可以说的再清楚些吗'
]

def handle(text):
	reply = random.choice(replies)
	# TO-DO: 
	return {'slot':res}

def isValid(text):
    return True
