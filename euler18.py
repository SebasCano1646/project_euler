x = open(r"C:\Users\Usuario.LAPTOP-VML067PV\Documents\ProjectEulerTXT\input_18.txt")

matrix = []

for line in x.readlines():
    list = line.replace("\n", "").split(" ")
    matrix.append(list)

def trip(x, y):
    if x == len(matrix)-1:
        return int(matrix[x][y])
    else:
        if trip(x+1, y) > trip(x+1, y+1):
            return int(matrix[x][y]) + trip(x+1, y)
        else:
            return int(matrix[x][y]) + trip(x+1, y+1)

print(trip(0,0))
