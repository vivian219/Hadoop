import sys
import json
nameList={}

jencode=json.JSONEncoder()
 
for line in sys.stdin:
    line=line.strip()
    key,value=line.split('\t',1)
    nameList.setdefault(key,[])
    nameList[key].append(value)
for x in nameList:
    for y in nameList[x]:
        if(nameList.has_key(y)&&x in nameList[y]):
            nameList[y].remove(x)
            nameList[x].remove(y)
for item in nameList:
    for ele in nameList[item]:   
        print jencode.encode(item+" "+ele)