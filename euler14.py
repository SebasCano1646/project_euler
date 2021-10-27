n = int(input("Tu numero: "))

def coll(x):
    if x%2 == 0:
        return int(x/2)
    else:
        return 3*x + 1

list = [1]

for i in range(2,n):
    count = 0
    num = i
    while True:
        if num < i:
            count += list[num-1]
            break
        else:
            num = coll(num)
            count += 1
    list.append(count)

ans = 0

for i in range(0, n-1):
    if list[i] > list[ans]:
        ans = i

print(ans+1)