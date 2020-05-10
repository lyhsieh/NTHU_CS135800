import operator as op
class Vector:
    def __init__(self, *v):
        self._v = list(v)
    def __repr__(self):
        return __class__.__name__ + repr(tuple(self._v))
    def __add__(self, right):
        return Vector(*map(op.add, self._v, right._v))
    def __sub__(self, right):
        return Vector(*map(op.sub, self._v, right._v))
    def __iadd__(self, right):
        self._v[:] = map(op.add, self._v, right._v)
        return self
    def __len__(self):
        return len(self._v)
    def __getitem__(self, i):
        if type(i) == int:
            return self._v[i]
        elif type(i) == slice:
            return Vector(*(self._v[i]))
        else:
            raise TypeError(type(i).__name__ + ' unsupported')
    def setitem(self, i, v):
        if type(i) == int:
            self._v[i] = v
        elif type(i) == slice:
            self.v[i] = v if not isinstance(v, Vector) else v._v[:]
        else:
            raise TypeError(type(i).__name__ + ' unsupported')
