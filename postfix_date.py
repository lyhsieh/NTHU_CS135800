import datetime
import operator as op

class days(datetime.timedelta):
    def __init__(self, d):
        super().__init__(days = d)
        self._d = d
    def __repr__(self):
        return f'days({d})'
     

def postcalc(*parameter):
    ans = []
    for i in parameter:
        if i == 'add':
            A = ans.pop()
            B = ans.pop()
            ans.append(A + B)
        elif i == 'sub':
            A = ans.pop()
            B = ans.pop()
            ans.append(A - B)
        elif i == 'swap':
            A = ans.pop()
            B = ans.pop()
            ans.append(A)
            ans.append(B)
        else:
            ans.append(i)
    return ans

