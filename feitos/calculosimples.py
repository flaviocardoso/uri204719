string1 = input()
string2 = input()

v1 = string1.split(" ")
v2 = string2.split(" ")

np1 = int(v1[1])
vu1 = float(v1[2])

np2 = int(v2[1])
vu2 = float(v2[2])

total = (np1 * vu1) + (np2 * vu2)

print("VALOR A PAGAR: R$ %.2f" % total)
