x = 1
y = 1
z = 0

sum = 0

while True:
    z = x + y
    
    if z > 4000000:
        break
    elif z%2 == 0:
        sum += z
    
    x = y
    y = z

print(sum)