def myPow(x, n):
    res = 1
    while n > 0:
        res *= x
        n -= 1
    return res

x = int(input("Enter the number: "))
n = int(input("Enter the power: "))
print(myPow(x, n))
