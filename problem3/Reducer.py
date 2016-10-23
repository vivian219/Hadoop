# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:36:18 2016

@author: vivian0219
"""
import sys
import json
nameList={}

jencode=json.JSONEncoder()
 
for line in sys.stdin:
    line=line.strip()
    key,value=line.split('\t',1)
    nameList.setdefault(key,[])
    nameList[key].append(value)
for item in nameList:
    print jencode.encode(item+'\t'+len(nameList[item]))
