import sys
import json

for line in sys.stdin:
    line=line.strip()
    record=json.loads(line)
    id=record[0]
    nuc=record[1]
    print '%s\t%s' % 