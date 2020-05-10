def print_indent(L, level = 0):
    for item in L:
        if type(item) == list:
            level_next = level + 1
            print_indent(item, level_next)
        else:   #which means item now is a string
            print(' ' * level * 4 + item)

s = input()
L = eval(s)
print_indent(L)
