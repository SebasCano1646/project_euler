from math import sqrt

def isabu(x):
    div = []
    count = 1
    while count < sqrt(x):
        if x%count  == 0:
            div.append(count)
            div.append(int(x/count))
        count += 1
    if count == sqrt(x):
        div.append(count)
    sum = 0
    for i in div:
        sum += i
    if sum > 2*x:
        return True
    else:
        return False

abundant = {}

for i in range(1,28123):
    if isabu(i):
        abundant[i] = True

def issum(x):
    for i in abundant:
        if x-i in abundant:
            return True
    return False

sum = 0

for i in range(1,28123):
    if not issum(i):
        sum += i

print(sum)