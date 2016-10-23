import sys
import json
dna={}
result=[]
for line in sys.stdin:
    line=line.strip()
    id,nuc=line.split('\t')
    nuc=nuc[:-10]
    dna.setdefault(nuc,[])
    if id not in dna[nuc]:
        dna[nuc].append(id)
jout=json.JSONEncoder()
for i in dna:
    print jout.encode(i)
    