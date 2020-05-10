def GenF():
    print('GenF')
    a = yield 1
    print('GenF a = ', repr(a))
    b = yield 2
    print('GenF b = ', repr(b))
    c = yield 3
    print('GenF c = ', repr(c))

def GenG():
    print('GenG')
    f = GenF()
    print('GenG constructed f')
    h = next(f)
    print('GenG started f')
    i = f.send('a')
    print('GenG sent a')
    j = f.send('b')
    print('GenG sent b')
    print('h i j = ', h, i, j)
