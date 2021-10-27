a = int(input("Cantidad de Filas: "))
b = int(input("Cantidad de Columnas: "))

def fac(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

print(fac(a+b)/(fac(a)*fac(b)))