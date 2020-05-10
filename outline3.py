def number_outline(L, prefix = ()):
    if callable(prefix) == True:
        format_list = prefix()
        prefix = ()
        if type(L) in {list, tuple}:
            i = 0
            for v in L:
                if type(v) not in {list, tuple}:
                    i += 1
                number_outline(v, prefix + (i,))
        else:
            s = ' ' * 4 * (len(prefix) - 1)
            if len(prefix) == 1:
                j = 0
                s += format_list[j]
                j += 1
            elif len(prefix) == 2:
                j = 0
                s += format_list[j]
                j += 1
            else:
                j = 0
                s += format_list[j]
                j += 1
            print('. ' + s)


    else:
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


def my_outline_format_function(level = 0):
    if level == 0:
        return ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    elif level == 1:
        return [chr(i) for i in range(65, 75)]
    else:
        return [i for i in range(1, 11)]

