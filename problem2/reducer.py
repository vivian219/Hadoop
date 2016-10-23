# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:25:00 2016

@author: vivian0219
"""
import sys
import json
 fileList={}
 result=[]
 jencode=json.JSONEncoder()
 
 for line in sys.stdin:
     line=line.strip()
     order_id,values=line.split('\t',1)
     value=json.loads(values)
     fileList.setdefault(order_id,[])
        fileList[order_id].append(values)
 for id in fileList:
     for value in fileList[id]:
         if value[0]=='order':
             order=value
     for value in fileList[id]:
         if value[0]=='line_item':
             result.append((order+value))
 for item in result:
     print jencode.encode(item)