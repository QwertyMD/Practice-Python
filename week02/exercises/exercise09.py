def prodNums(*n):
    pro = 1
    for i in n:
        pro *= i
    return pro

print(prodNums(1, 2, 3, 4, 5))
print(prodNums(12, 13, 14))
