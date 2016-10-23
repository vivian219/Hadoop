# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:24:26 2016

@author: vivian0219
"""
import sys
import json

jenc=json.JSONEncoder()
for line in sys.stdin:
    line=line.strip()
    record=json.loads(line)
    key=jenc.encode(record[1])
    value=jenc.encode(record)
    print '%s\t%s' % (key,value)
