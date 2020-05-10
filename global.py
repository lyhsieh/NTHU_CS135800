a = 3
def F():
    global a
    print(a)
    a = 5
print(a)
F()
print(a)
