def rec_find(L, val):
    if type(L) in {list, tuple}:
        for i, v in enumerate(L):
            p = rec_find(v, val)
            if p == True:
                return (i,)
            if p != False:
                return (i,) + p
    return L == val


