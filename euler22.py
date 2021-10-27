x = open(r"C:\Users\Usuario.LAPTOP-VML067PV\Documents\ProjectEulerTXT\input_22.txt")

alpha = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23,'X' : 24, 'Y' : 25, 'Z' : 26}

names = x.read().split(",")

count = 0
for name in names:
    names[count] = name.replace("\"","")
    count += 1

print(names)

def value(name):
    val = 0
    for letter in name:
        val += alpha[i]
    return val

def min(a, b):
    count = 0
    while True:
        if count >= len(a) and count >= len(b):
            return a
        if count >= len(a):
            return a
        if count >= len(b):
            return b
        if alpha[a[count]] > alpha[b[count]]:
            return b
        if alpha[b[count]] > alpha[a[count]]:
            return a
        else:
            count += 1

ordered = []

while len(names) > 0:
    first = names[0]
    for name in names:
        if min(first, name) != first:
            first = name
    ordered.append(first)
    names.remove(first)

sum = 0
x = 1

for name in ordered:
    name_value = 0
    for letter in name:
        name_value += alpha[letter]
    sum += x*name_value
    x += 1

print(sum)
