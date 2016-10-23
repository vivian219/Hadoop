import sys
import json

maxI = 10
maxJ = 10
jencode json.JSONEncoder()

for line in sys.stdin:
    line=line.strip()
    record=json.loads(line)
    if record[0]=='a':
        i=record[1]
        for j in range(maxJ+1):
            print '%s\t%s\t%s' % (i,j,jencode.encode(record))
    elif record[0]=='b':
        j=record[2]
        for i in range(maxI+1):
            print '%s\t%s\t%s' % (i,j,jencode.encode(record))
    else:
        pass
        