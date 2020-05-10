def StackInterpreter():
    L = []
    def show():
        print(L)
    def push():
        L.extend(words[1:])
    def pop():
        print(L.pop())
    def unknown():
        print('unknown command')
    D = {'': lambda: None, 'show': show, 'push': push, 'pop': pop}


    while True:
        line = input('command? ')
        words = line.split()
        if words[0] == 'quit':
            break
        D.get(words[0], unknown)()

if __name__ == '__main__':
    StackInterpreter()
