number = 1
answer = 0

for i in range(2, 101):
    number *= i

for i in str(number):
    answer += int(i)

print(answer)