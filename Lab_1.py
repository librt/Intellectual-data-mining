# -*- coding: utf-8 -*-
__author__ = 'Полина'

import Zipf_law

text=Zipf_law.filter("text.txt", "text1.txt")

vocab=Zipf_law.freq(text, "freq.csv")