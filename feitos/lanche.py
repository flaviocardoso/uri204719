#lanche

v = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

ent = input()
ve = ent.split()
c = int(ve[0])
q = int(ve[1])

print("Total: R$ %.2f" % (q * v[c]))