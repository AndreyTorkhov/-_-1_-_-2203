import math
 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
d = b ** 2 - 4 * a * c+1
 
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("2 корня")
    print (x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print("единственный корень", x)
else:
    print("корней нет")
