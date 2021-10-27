number = 0

def rev(x):
    list = []
    for y in x:
        list.append(y)

    list.reverse()

    number =""
    count = 0

    for y in list:
        number = number + list[count]
        count += 1
    return number

for n in range(110, 1000, 11):
    for m in range(100, 1000):
        r = rev(str(m*n))
        if int(r) == m*n and m*n > number:
            number = m*n

print(number)