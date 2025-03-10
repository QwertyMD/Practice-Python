def primeCheck(n):
    if n < 2:
        return "Neither Prime or Composite"
    else:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        return "Prime" if count == 2 else "Composite"

num = int(input("Enter a number: "))
print(primeCheck(num))
