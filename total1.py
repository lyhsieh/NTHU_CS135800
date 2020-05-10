#!/usr/bin/env python3
D = { 'rate': 0.0 }

def totalWithTax(*names, **kv):
    global D
    total = 0.0
    for name in names:
        total += D[name]
    for kw, val in kv.items():
        D[kw] = val # overwrite dict entry
        if kw != 'rate':
            total += val
    return total * (1 + D['rate'])
