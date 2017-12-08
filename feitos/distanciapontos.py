from math import sqrt

dado1 = input()
dado2 = input()

x1, y1 = dado1.split(" ")
x2, y2 = dado2.split(" ")

x = pow((float(x2) - float(x1)), 2)
y = pow((float(y2) - float(y1)), 2)

dis = sqrt(x + y)

print("%.4f" % dis)