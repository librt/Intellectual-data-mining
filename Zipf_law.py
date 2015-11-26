# -*- coding: utf-8 -*-
__author__ = 'Полина'

import re
import codecs

def filter(name, fname):
    with codecs.open(name, 'r', 'utf-8') as t:
        text = t.read()
        text = text.lower()
        text = re.sub(u'[^a-zа-яё]', ' ', text)
        text = re.sub(r' +', ' ', text)
        #with codecs.open(fname, 'w', 'utf-8') as f:
        #   f.write(text) //запись в файл
    return text

def freq(text):
    vocab={}
    for word in re.findall(ur'[a-zа-яё]+', text):
        if word not in vocab:
            vocab[word]=0
        vocab[word]+=1
    for word in vocab:
        print word, vocab[word]



