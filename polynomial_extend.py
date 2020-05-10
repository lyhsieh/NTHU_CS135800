import operator as op

class Polynomial:
    def __init__(self, *coeff):
        self._coeff = list(coeff)
    def __repr__(self):
        return self.__class__.__name__ + f"({', '.join(map(str, self._coeff))})"
    def evaluate(self, xvalue):
        return sum([a * xvalue ** i for i, a in enumerate(self._coeff)])
    __call__ = evaluate
    


    def __add__(self, RHS):
        L = []
        for i in range(max(len(self._coeff), len(RHS._coeff))):
            try:
                L.append(self._coeff[i] + RHS._coeff[i])
            except IndexError:
                 L.append(self._coeff[i] if len(self._coeff) > len(RHS._coeff) else RHS._coeff[i])
        return Polynomial(*L)

    def __sub__(self, RHS):
        L = []
        for i in range(max(len(self._coeff), len(RHS._coeff))):
            try:
                L.append(self._coeff[i] - RHS._coeff[i])
            except IndexError:
                 L.append(-RHS._coeff[i] if len(self._coeff) < len(RHS._coeff) else self._coeff[i])
        return Polynomial(*L)

    def __imul__(self, scalar):
        return Polynomial(*map(lambda x: scalar * x, self._coeff))

instantiate_f = input()
exec(instantiate_f)
instantiate_g = input()
exec(instantiate_g)
print_f_add_g = input()
exec(print_f_add_g)
print_g_sub_f = input()
exec(print_g_sub_f)
f_scale = input()
exec(f_scale)
print_f = input()
exec(print_f)
print_f_eval = input()
exec(print_f_eval)

