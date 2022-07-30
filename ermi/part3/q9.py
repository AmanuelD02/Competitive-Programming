import math
a, b, c = eval(input())

x1 = (-b + math.sqrt( (b*b) - (4*a*c) )) / 2*a
x2 = (-b - math.sqrt( (b*b) - (4*a*c) )) / 2*a
print(x1, x2)