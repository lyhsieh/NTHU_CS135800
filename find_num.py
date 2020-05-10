for i in range(1000, 10000):
    digit = str(i)
    d0 = int(digit[0])
    d1 = int(digit[1])
    d2 = int(digit[2])
    d3 = int(digit[3])
    if '0' not in digit and d0 ** d0 + d1 ** d1 + d2 ** d2 + d3 ** d3 == i:
        print(i)
    
