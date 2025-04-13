def fib(n):
    if n <= 1:
        print(0)
    else:
        a = 0
        b = 1
        c = 0
        print(a)
        print(b)
        for i in range(n - 2):
            c = a + b
            print(c)
            a = b
            b = c

num = int(input("Enter the nth term of the fibonacci series: "))
fib(num)
