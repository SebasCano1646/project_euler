def pyt(x, y, z):
    if (x**2 == y**2 + z**2) or (y**2 == x**2 + z**2) or (z**2 == x**2 + y**2):
        return True
    else:
        return False

for x in range (1,1000):
    for y in range(1,1000):
        z = 1000 - x - y
        if z > 0 and pyt(x, y, z):
            print(x*y*z)