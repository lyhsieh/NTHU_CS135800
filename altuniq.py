#!/usr/bin/env python3.7
import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 2:
    sys.stderr.write(f'Usage: {sys.argv[0]} imputFile\n')
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as fh:
        previousLine = ''   #initialize
        for line in fh.readlines():
            if line != previousLine:    #filter
                print(line, end = '')
            previousLine = line     #update previous

except OSError as err:
    sys.stderr.write(str(err) + '\n')
    sys.exit(2)
