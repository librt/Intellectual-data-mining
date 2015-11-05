# -*- coding: utf-8 -*-
__author__ = 'Полина'

import re
import codecs

with codecs.open("D://text.txt", 'r', 'utf-8') as t:
    text = t.read()
    text = text.lower()
    text = re.sub(u'[^a-zа-яё]', ' ', text)
    print(text)
    with codecs.open("D://text1.txt", 'w', 'utf-8') as f:
        f.write(text)
