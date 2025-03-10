def decToBin(n):
    lst = list()
    while n != 0:
        bit = n % 2
        lst.insert(0, bit)
        n = n // 2
    return lst

num = int(input("Enter a number: "))
if num == 0:
    print(0)
else:
    for i in decToBin(num):
        print(i, end="")
