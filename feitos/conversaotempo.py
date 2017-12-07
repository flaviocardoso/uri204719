tt = int(input())

h = 0
m = 0
s = 0

h = tt / 3600
tt = tt % 3600
m = tt / 60
s = tt % 60

print("%d:%d:%d" % (h, m, s))