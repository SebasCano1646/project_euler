count = 0
day = 2

for year in range(1901,2001):
    for month in range(1,13):
        if day == 0:
            count += 1
        if month in [1, 3, 5, 7,8,10,12]:
            day = (day+31) % 7
        elif month in [4, 6, 9, 11]:
            day = (day+30) % 7
        elif year%4 == 0 and year%100 != 0:
            day = (day+29) % 7
        elif year%400 == 0:
            day = (day+29) % 7
        else:
            day = (day+28) % 7

print(count)