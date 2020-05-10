# ax^2 - 2bx + c = 0
# rolling a fair die 3 times
# the result are a, b, c respectively
# calc the prob of two distinct real roots
cnt = 0
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            delta = 4 * b * b - 4 * a * c
            if delta > 0:
                print(f'a = {a}, b = {b}, c = {c}')
                cnt += 1
print(f'cnt = {cnt}')
