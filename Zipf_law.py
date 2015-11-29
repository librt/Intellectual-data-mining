# -*- coding: utf-8 -*-
from os import linesep

__author__ = 'Полина'

import re
import codecs
from operator import itemgetter
import csv


def filter(name, fname):
    with codecs.open(name, 'r', 'utf-8') as t:
        text = t.read()
        text = text.lower()
        text = re.sub(u'[^a-zа-яё]', ' ', text)
        text = re.sub(r' +', ' ', text)
        #with codecs.open(fname, 'w', 'utf-8') as f:
        #   f.write(text) //запись в файл
    return text

def freq(text, file_name):
    vocab={}
    for word in re.findall(ur'[a-zа-яё]+', text):
        if word not in vocab:
            vocab[word]=0
        vocab[word]+=1

    result=sorted(vocab.iteritems(), key=lambda x: x[1], reverse=True)
    print linesep.join('%s,%d'%r for r in result)

    with codecs.open(file_name, 'wb', 'utf-8') as t:
            writer=csv.writer(t, delimiter=';', quoting=csv.QUOTE_ALL)
            for i in result:
                writer.writerow([i[1]])



