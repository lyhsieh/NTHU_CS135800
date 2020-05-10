class CountingList(list):
    def __init__(self, d = []):
        super().__init__(d)
        self._listin = d
        self._count = [0 for i in range(len(d))]

    def __getitem__(self, i):
        if type(i) == int:
            self._count[i] += 1
        else:   #which means type(i) is a slice
            '''
            start, stop, step = i.start, i.stop, i.step
            while start < stop:
                self._count[start] += 1
                if step == None:
                    start += 1
                else:
                    start += step
                '''
            self._count[i] = map(lambda x: x + 1, self._count[i])
        return super().__getitem__(i)

    def __iter__(self):
        L = list(zip(self._count, self._listin))
        L.sort(reverse = True)
        ans = [i[1] for i in L]
        it = iter(ans)
        return it
