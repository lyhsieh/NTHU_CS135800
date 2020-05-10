def fib():
    yield 0    #for n = 0
    yield 1    #for n = 1
    fn_minus_2 = 0
    fn_minus_1 = 1
    n = 2
    while True:
        fn = fn_minus_2 + fn_minus_1
        yield fn
        fn_minus_2, fn_minus_1 = fn_minus_1, fn
