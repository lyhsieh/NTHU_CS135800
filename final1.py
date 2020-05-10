s = input()
L = s.split()
for item in L:
    if ord('A') <= ord(item[0]) <= ord('Z'):
        if '.' in item:
            print(item[:-1])
        else:
            print(item)
