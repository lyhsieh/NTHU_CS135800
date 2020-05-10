import sys

def print_operation_list():
    try: 
        with open('Operation_list.txt', 'r') as fh:
            for lines in fh.readlines():
                print(lines, end = '')
    except FileNotFoundError:
        sys.stderr.write('cannot open Operation_list.txt\n')

def look():
    try:
        with open('Tiki_line.txt', 'r') as fh:
            i = 1
            for lines in fh.readlines():
                print(f'#{i} ' + lines, end = '')
                i += 1
    except FileNotFoundError:
        sys.stderr.write('cannot open tiki_line.txt\n')

def tiki_up_1():
    color = input('Select your target color: ')
    L = []
    try:
        with open('Tiki_line.txt', 'r') as fh1:
            L = fh1.readlines()
            target =  L.index(f'{color}\n')
            assert target >= 1
            L[target - 1], L[target] = L[target], L[target - 1]
        with open('Tiki_line.txt', 'w') as fh2:
            fh2.write(''.join(L))
    except ValueError:
        sys.stderr.write('Error: Invalid target\n')
    except AssertionError:
        sys.stderr.write("Error: You can't do this operation.\n")

def tiki_up_2():
    color = input('Select your target color: ')
    L = []
    try:
        with open('Tiki_line.txt', 'r') as fh1:
            L = fh1.readlines()
            target =  L.index(f'{color}\n')
            assert target >= 2
            L[target - 2], L[target - 1], L[target] = \
            L[target], L[target - 2], L[target - 1]
        with open('Tiki_line.txt', 'w') as fh2:
            fh2.write(''.join(L))
    except ValueError:
        sys.stderr.write('Error: Invalid target\n')
    except AssertionError:
        sys.stderr.write("Error: You can't do this operation.\n")

def tiki_up_3():
    color = input('Select your target color: ')
    L = []
    try:
        with open('Tiki_line.txt', 'r') as fh1:
            L = fh1.readlines()
            target =  L.index(f'{color}\n')
            assert target >= 3
            L[target - 3], L[target - 2], L[target - 1], L[target] = \
            L[target], L[target - 3], L[target - 2], L[target - 1]
        with open('Tiki_line.txt', 'w') as fh2:
            fh2.write(''.join(L))
    except ValueError:
        sys.stderr.write('Error: Invalid target\n')
    except AssertionError:
        sys.stderr.write("Error: You can't do this operation.\n")

def tiki_topple():
    color = input('Select your target color: ')
    L = []
    try:
        with open('Tiki_line.txt', 'r') as fh1:
            L = fh1.readlines()
            assert f'{color}\n' in L
            L.append(f'{color}\n')
            L.remove(f'{color}\n')
        with open('Tiki_line.txt', 'w') as fh2:
            fh2.write(''.join(L))
    except AssertionError:
        sys.stderr.write('Error: Invalid target\n')

def tiki_toast():
    L = []
    try:
        with open('Tiki_line.txt', 'r') as fh1:
            L = fh1.readlines()
            assert len(L) >= 4
            L.pop()
        with open('Tiki_line.txt', 'w') as fh2:
            fh2.write(''.join(L))
    except AssertionError:
        sys.stderr.write("Error: You can't do this operation.\n")

def reset():
    try:
        with open('Tiki_line.txt', 'w') as fh:
            fh.write('red\nyellow\nblue\ngreen\npurple\npink\norange\nbrown\ngrey\n')
    except FileNotFoundError:
        sys.stderr.write('cannot open tiki_line.txt\n')

def unknown():
    print('unknown command')

if __name__ == '__main__':
    D = {'': lambda: None, 'help': print_operation_list, 'look': look, \
         'Tiki up 1': tiki_up_1, 'Tiki up 2': tiki_up_2, \
         'Tiki up 3': tiki_up_3, 'Tiki Topple': tiki_topple, \
         'Tiki Toast': tiki_toast, 'Reset': reset}

    while True:
        command = input("What's your operation? ")
        if command == 'quit':
            break
        D.get(command, unknown)()
