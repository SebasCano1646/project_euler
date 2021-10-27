num = 1

for x in range(1, 21):
    mul = 1
    while ((num*mul) % x) != 0:
        mul += 1
    num = num*mul

print(num)