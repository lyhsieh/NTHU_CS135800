def StackInterpreter():
    L = []
    D = {'':     lambda: None, 
         'show': lambda: print(L), 
         'push': lambda: L.extend(words[1:]), 
         'pop':  lambda: print(L.pop()) }
    while True:
        line = input('command? ')
        words = line.split()
        if words[0] == 'quit':
            break
        D.get(words[0], lambda: print('unknown command'))

if __name__ == '__main__':
    StackInterpreter()
