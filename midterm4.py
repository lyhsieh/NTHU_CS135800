name = input()
print(f'My name is {name}.')
print('Spell my name in reverse order: ', end = '')
for n in range(len(name)):
    print(name[len(name) - n - 1], end = '')
    if n != len(name) - 1:
        print('-', end = '')
print()
