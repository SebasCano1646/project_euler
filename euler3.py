x = int(input())

prime = 1
count = 2

while count <= x:
    if x%count == 0:
        x = x / count
        prime = count
    else:
        count += 1

print(prime)