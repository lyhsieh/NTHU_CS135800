def aporgp(ser):
    if int(ser[3]) + int(ser[0]) == int(ser[1]) + int(ser[2]):
        d = int(ser[3]) - int(ser[2])
        print(' '.join(ser) + f' {int(ser[3]) + d}')
    else:
        r = int(ser[3]) / int(ser[2])
        print(' '.join(ser) + f' {int(int(ser[3]) * r)}')

if __name__ == '__main__':
    prob = int(input())
    series_all = []
    for i in range(prob):
        #series = []
        list_in = input().split()
        series_all.append(list_in)
        #for ch in list_in:
            #series.append(ch)
        #aporgp(*series_all)
    for series in series_all:
        aporgp(series)
