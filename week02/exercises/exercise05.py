from exercise04 import sumOfDivisors

def checkPerfectNum(n):
    return sumOfDivisors(n) == n

num = int(input("Enter a number: "))
print("Perfect Number") if checkPerfectNum(num) else print("Not a perfect number")