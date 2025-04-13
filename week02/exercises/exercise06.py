def calcMean(lst):
    return sum(lst)/len(lst)

def calcMedian(lst):
    lst.sort()
    return lst[len(lst)//2]

marks = [20, 30, 35, 55, 70, 80, 90]
print(calcMean(marks))
print(calcMedian(marks))