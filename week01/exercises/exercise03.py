def sumDigits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    print(sum)

num = int(input("Enter any digit: "))
sumDigits(num)
