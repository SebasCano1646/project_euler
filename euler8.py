x = open(r"C:\Users\Usuario.LAPTOP-VML067PV\Documents\ProjectEulerTXT\input_8.txt")

list = x.readlines()

num = ""

for line in list:
    num = num + line

num = num.replace("\n", "")

ans = 1

for x in range(len(num)-12):
    calc = 1
    for i in range(13):
        calc = calc*int(num[x+i])
    if calc > ans:
        ans = calc

print(ans)