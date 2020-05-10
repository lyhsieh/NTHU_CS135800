def atom_gen(L):
    if L is None:
        return 
    if type(L) in {list, tuple}:
        for child in L:
            for atom in atom_gen(child):
                yield atom
    else:
        yield L
