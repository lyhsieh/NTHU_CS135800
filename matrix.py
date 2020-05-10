import random
import operator as op

random.seed(0)

class Matrix:
    def __init__(self, data):
        self._row = data
        self._col = list(map(list, list(zip(*data))))
    
    def __repr__(self):
        return __class__.__name__ + f'{self._row}'

    def row(self, r):
        return self._row[r]

    def column(self, c):
        return self._col[c]

    @property
    def nrows(self):
        return len(self._row)

    @property
    def ncolumns(self):
        return len(self._col)

    def transpose(self):
        new_row = self._col
        return Matrix(self._col)

    def randomize(self):
        flatten = []
        new_row_list = []
        for row in self._row:
            flatten.extend(row)
        random.shuffle(flatten)
        for i in range(len(self._row)):
            new_row_list.append(flatten[0: len(self._row) + 1])
            del flatten[0: len(self._row) + 1]
        return Matrix(new_row_list)

    def __matmul__(self, other):
        L = []
        new_row_list = []
        row = self._row
        column = other._col
        if self.ncolumns == other.nrows:
            for i in range(self.nrows):
                for j in range(other.ncolumns):
                    element = sum(map(op.mul, row[i], column[j]))
                    L.append(element)
            for j in range(len(self._row)):
                new_row_list.append(L[0: other.ncolumns])
                del L[0: other.ncolumns]
            return Matrix(new_row_list)
        else:
            raise ValueError('These two matrix are not multipliable.')

    instantiate_M = input()

    exec(instantiate_M)

    randomize_M = input()

    exec(randomize_M)

    print_row_M = input()

    exec(print_row_M)

    instantiate_N = input()

    exec(instantiate_N )

    transpose_N = input()

    exec(transpose_N )

    print_row_N = input()

    exec(print_row_N)

    calculate_M_multiply_N = input()

    exec(calculate_M_multiply_N)

    print_row_O = input()

    exec(print_row_O)
