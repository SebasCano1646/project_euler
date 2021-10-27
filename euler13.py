x = open(r"C:\Users\Usuario.LAPTOP-VML067PV\Downloads\input_13.txt")

sum = 0

for line in x.readlines():
    sum += int(line)

print(str(sum)[0:10])
