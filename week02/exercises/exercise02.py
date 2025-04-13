def primeCheck(n):
    count = 0
    for i in range(1, n + 1):
        count += 1 if n % i == 0 else 0
    return count == 2

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Neither Prime or Composite") if num < 2 else print("Prime") if primeCheck(num) else print("Composite")
