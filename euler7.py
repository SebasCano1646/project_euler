from math import sqrt

primelist = []

def isprime(p):
    test = 2
    while test <= sqrt(p):
        if p%test == 0:
            return False
        test += 1
    return True

num = 2

while len(primelist) < 10001:
    if isprime(num):
        primelist.append(num)
    num += 1

primelist.reverse()

print(primelist[0])