'''find the roots of a*x^2 + b*x + c = 0'''
import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

delta = b * b - 4 * a * c

if delta > 0:
    x1 = int((-b + math.sqrt(delta)) / (2 * a))
    x2 = int((-b - math.sqrt(delta)) / (2 * a))
    print(f'Two different roots x1={x1} , x2={x2}', end = '')
elif delta == 0:
    x = int(-b / (2 * a))
    print(f'Two same roots x={x}')
else:
    print('No real root', end = '')
