def number_outline(L, prefix = ()):
    if type(L) in {list, tuple}:
        i = 0
        for v in L:
            if type(v) not in {list, tuple}:
                i += 1
            number_outline(v, prefix + (i,))
    else:
        s = ' ' * 4 * (len(prefix) - 1)
        s += '.'.join(map(str, prefix))
        s += '. ' + L
        print(s)

