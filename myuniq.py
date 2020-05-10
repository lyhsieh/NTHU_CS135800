#!/usr/bin/env python3.7
import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 2:
    sys.stderr.write('Usage: %s imputFile\n' % sys.argv[0])
    sys.exit(1)
try:
    fh = open(sys.argv[1], 'r')     #fh means 'file handle'
except:
    sys.stderr.write('cannot open input file %s' % sys.argv[1])
    sys.exit(2)
previousLine = ''   #initialize
for line in fh.readlines():
    if line != previousLine:    #filter
        print(line, end = '')
    previousLine = line     #update previous
fh.close()
