# -*- coding: utf-8 -*-
__author__ = 'Полина'

import re
import codecs

def filter(textname="name"):
    with codecs.open(textname, 'r', 'utf-8') as t:
        text = t.read()
        text = text.lower()
        text = re.sub(u'[^a-zа-яё]', ' ', text)
        text = re.sub(r' +', ' ', text)
        print(text)
        with codecs.open("textname1.txt", 'w', 'utf-8') as f:
            f.write(text)