import sys
while True:
    exp = input('Enter an expression: ')
    if exp == 'quit':
        print('Goodbye!')
        break
    else:
        try:
            assert '+' in exp or '-' in exp or '*' in exp or '/' in exp
            print('Answer: ', end = '')
            print(f'{eval(exp):.2f}' if type(eval(exp)) != int else f'{eval(exp)}')
        except ZeroDivisionError:
            sys.stderr.write('Error: Cannot divide by 0\n')
        except:
            sys.stderr.write('Error: Invalid expression\n')
