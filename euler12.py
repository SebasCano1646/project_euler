from math import sqrt
from math import ceil

def tri(x):
    return x*(x+1)/2

def div(x):
    bound = ceil(sqrt(x))
    divisors = 0
    for i in range(1, bound+1):
        if i == sqrt(x):
            divisors += 1
        elif x%i == 0:
            divisors += 2
    return divisors

count = 1

while div(tri(count)) <= 500:
    count += 1

print(int(tri(count)))