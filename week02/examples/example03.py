def a(s1):
    return len(s1)

def b(s2):
    return sum(s2)

def c(s1, s2, s3):
    return s1 | s2 | s3

def d(s1, s2, s3):
    return s1 & s2 & s3

def e(s1, s2):
    return s1 - s2

def f(s2, s3):
    return s2 - s3

def g(s1, s2, s3):
    return s3.issubset(s1), s3.issubset(s2)

def h(su, s1):
    return su - s1

def i(s1):
    for x in s1:
        if x == 15:
            return True
    return False

def j(s1):
    s1.add(60)
    return s1

def k(s2):
    s2.discard(60)
    return s2

def l(s3):
    s3.clear()
    return s3

def m(s2):
    return max(s2), min(s2)

setU = set(range(1, 51))
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {10, 20, 30}

print(f"Length of set 1: {a(set1)}")
print(f"Sum of set 2: {b(set2)}")
print(f"Union: {c(set1, set2, set3)}")
print(f"Intersection: {d(set1, set2, set3)}")
print(f"set1 - set2: {e(set1, set2)}")
print(f"set2 - set3: {f(set2, set3)}")
print(f"set3 is subset of set1, set2: {g(set1, set2, set3)}")
print(f"Complement of set1: {h(setU, set1)}")
print(f"15 is present in set1: {i(set1)}")
print(f"set 1 with 60 added: {j(set1)}")
print(f"set 2 with 60 removed: {k(set2)}")
print(f"set 3 with all elements removed: {l(set3)}")
print(f"max and min value in set 2: {m(set2)}")
