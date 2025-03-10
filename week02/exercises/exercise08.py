def prodDigits(n):
    pro = 1
    while n != 0:
        rem = n % 10
        pro *= rem
        n = n // 10
    return pro

num = int(input("Enter a number: "))
print(0) if num == 0 else print(prodDigits(num))