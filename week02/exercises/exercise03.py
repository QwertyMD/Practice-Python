def primeCheck(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return True if count == 2 else False

def twinPrimes(length):
    for i in range(length):
        if primeCheck(i) and primeCheck(i + 2):
            print(f"{i}, {i + 2}")

twinPrimes(1000)
