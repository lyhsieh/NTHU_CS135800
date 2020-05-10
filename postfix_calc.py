def postcalc(*parameter, stack = []):
    L = stack + list(parameter)
    ans = []
    for i in L:
        if i == 'add':
            A = ans.pop()
            B = ans.pop()
            ans.append(A + B)
        elif i == 'sub':
            A = ans.pop()
            B = ans.pop()
            ans.append(A - B)
        elif i == 'mul':
            A = ans.pop()
            B = ans.pop()
            ans.append(A * B)
        elif i == 'swap':
            A = ans.pop()
            B = ans.pop()
            ans.append(A)
            ans.append(B)
        else:
            ans.append(i)
    return ans

