indent_level = 0
def number_outline(L, format_function):
    global indent_level

    if type(L) in {list, tuple}:
        for v in L:
            if type(v) not in {list, tuple}:
                number_outline(v, )

    else:   #when an element is detected
        s = ' ' * 4 * (len(prefix) - 1)
        s += '.'.join(map(str, prefix))
        s += '. ' + L
        print(s)


def my_outline_format_function(level):
    if level == 0:
        return ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    elif level == 1:
        return [chr(i) for i in range(65, 75)]
    else:
        return [i for i in range(1, 11)]
