x = open(r"C:\Users\Usuario.LAPTOP-VML067PV\Documents\ProjectEulerTXT\input_11.txt")

matrix = []

for line in x.readlines():
    a = line.replace("\n", "").split(" ")
    b = []
    for num in a:
        b.append(int(num))

    matrix.append(b)

max = 0

for line in range(0,20):
    for column in range(0, 20):
        if (line+3 < 20):
            multi = matrix[line][column]*matrix[line+1][column]*matrix[line+2][column]*matrix[line+3][column]
            if multi > max:
                max = multi
                print(max)
        if (column+3 < 20) and (line+3 <20):
            multi = matrix[line][column]*matrix[line+1][column+1]*matrix[line+2][column+2]*matrix[line+3][column+3]
            if multi > max:
                max = multi
                print(max)
        if (column-3 >= 0) and (line+3 < 20):
            multi = matrix[line][column]*matrix[line+1][column-1]*matrix[line+2][column-2]*matrix[line+3][column-3]
            if multi > max:
                max = multi
                print(max)
        if (column+3 < 20):
            multi = matrix[line][column]*matrix[line][column+1]*matrix[line][column+2]*matrix[line][column+3]
            if multi > max:
                max = multi
                print(max)

print(max)