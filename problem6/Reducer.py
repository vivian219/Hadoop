import sys
import json

mat={}
for line in sys.stdin:
    line=line.strip()
    k1,k2,values=line.split('\t',2)
    values=json.loads(values)
    mat.setdefault((k1,k2),[])
    mat[(k1,k2)].append(values)
for k in mat:
    values=list(mat[k])
    def f1(x):return x[0]=='a'
    def f2(x):return x[0]=='b'
    a_rows=filter(f1,values)
    b_rows=filter(f2,values)
    result=0
    for a in a_rows:
        for b in b_rows:
            if(a[2]==b[1]):
                result+=a[3]*b[3]
    if(result !=0):
        print '%s,%s,%s' % (k[0],k[1],result)