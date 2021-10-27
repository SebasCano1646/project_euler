from math import sqrt

def isprime(p):
    if p < 2:
        return False
    div = 2
    while div <= sqrt(p):
        if p%div == 0:
            return False
        div += 1
    return True

sum = 2

for i in range(3, 2000000, 2):
    if isprime(i):
        sum += i

print(sum)