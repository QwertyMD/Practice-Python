def sumOfDivisors(n):
    sum = 0
    for i in range(1, n):
        sum += i if n % i == 0 else 0
    return sum

if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    print(sumOfDivisors(num))
