def digit(x): #letras de one to nine
    if x==1 or x==2 or x==6:
        return int(3)
    elif x==4 or x==5 or x==9:
        return int(4)
    elif x==7 or x==8 or x==3:
        return int(5)

def ten(x): #letras de twenty to ninety
    if x==4 or x==5 or x==6:
        return int(5)
    if x==2 or x==3 or x==8 or x==9:
        return int(6)
    if x==7:
        return int(7)

def letter(x):
    count = 0
    #cambiando a string de 3 digitos
    y = ""
    if x < 10:
        y = "00" + str(x)
    elif x < 100:
        y = "0" + str(x)
    else:
        y = str(x)
    #adding centena
    if int(y[0]) != 0:
        count += 7
        count += digit(int(y[0]))
        if int(y[1:3]) != 0: #adding "and"
            count += 3
    if int(y[1]) == 0:
        if int(y[2]) == 0: #si la decena es 0
            return count
        return count + digit(int(y[2]))
    if int(y[1]) == 1: #si la decena es 1
        if int(y[1:3]) == 10:
            return count + 3
        if int(y[1:3]) == 11 or int(y[1:3]) == 12:
            return count + 6
        if int(y[1:3]) == 15 or int(y[1:3]) == 16:
            return count + 7
        if int(y[1:3]) == 13 or int(y[1:3]) == 14 or int(y[1:3]) == 18 or int(y[1:3]) == 19:
            return count + 8
        if int(y[1:3]) == 17:
            return count + 9
    count = count + ten(int(y[1])) #si la decena es cualquier otro numero
    if int(y[2]) != 0:
        count += digit(int(y[2])) #adding unidad
    return count

answer = 0

for i in range(1,1000):
    answer += letter(i)

print(answer+11) #add "one thousand and print answer"