import math

print('ax^2 + bx + c')
a = int(raw_input('Podaj a: '))
b = int(raw_input('Podaj b: '))
c = int(raw_input('Podaj c: '))
delta = b * b - (4 * a * c)

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print ('x1 = '), x1
    print ('x2 = '), x2
elif delta == 0:
    x1 = -b / (2 * a)
    print ('x1 = '), x1
else:
    print ('brak pierwiastkow')
