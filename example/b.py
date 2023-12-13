def fib(n):
    print("b.pyの呼び出し")
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b

    print()