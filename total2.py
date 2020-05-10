#!/usr/bin/env python3
D = {'rate': 0.0}
def totalWithTax(*names, **kv):    #"names" is a tuple and 
                                   #"kv" is a key-value pair
    global D
    total = 0.0
    for name in names:
        if type(name) in {int, float}:
            total += name
        else:
            total += D[name]

    for kw, val in kv.items():
        D[kw] = val    #overwrite dict entry
        if kw != 'rate':
            total += val

    return total * (1 + D['rate'])

if __name__ == '__main__':
    assert totalWithTax(rate=0.05, apple=20, oranges=15, guava=12) == 49.35
    assert totalWithTax('apple', 'guava') == 33.6
    assert totalWithTax(23, 45, 'oranges', mango=60) == 150.15
    #print(totalWithTax(rate = 0.05, apple = 20, orange = 15, guava = 12))
    
