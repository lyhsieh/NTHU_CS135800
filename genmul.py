import sys
L = sys.argv
try:
    a = int(L[1])
    b = int(L[2])
    filename = L[3]
    with open(filename, 'w') as fh:
        for i in range(a):
            new_list = [str((i + 1) * j) for j in range(1, b + 1)]
            fh.write(' '.join(new_list) + '\n')
except:
    sys.stderr.write('Invalid argument.')
