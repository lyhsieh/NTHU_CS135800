class Polynomial:
    def __init__(self, *coeff):
        self.coefficient = coeff
    def evaluate(self, xvalue):
        ans = 0
        j = 0
        for i in self.coefficient:
            ans += i * (xvalue ** j)
            j += 1
        return ans
