from math import sqrt
ami = []

def seb(x):
    if x == 1:
        return 0
    divisors = []
    div = 2
    while div < sqrt(x):
        if x%div == 0:
            divisors.append(div)
            divisors.append(int(x/div))
        div += 1
    if div == sqrt(x):
        divisors.append(div)
    sum = 0
    for i in divisors:
        sum += i
    return sum+1

for i in range(2, 10000):
    if not i in ami:
        if seb(seb(i)) == i and seb(i) != i:
            ami.append(i)
            ami.append(seb(i))

sum = 0

for i in ami:
    sum += i

print(sum)