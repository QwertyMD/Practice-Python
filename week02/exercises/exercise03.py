from exercise02 import primeCheck

def twinPrimes(length):
    for i in range(length):
        if primeCheck(i) and primeCheck(i + 2):
            print(f"{i}, {i + 2}")

twinPrimes(1000)
