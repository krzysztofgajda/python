import math

x = int(raw_input('Podaj liczbe naturalna: '))
if x % math.sqrt(x) == 0:
    print 'posiada pierwiastek'
else:
    print 'nie posiada pierwiastka'
