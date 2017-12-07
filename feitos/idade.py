id = int(input())

a = id / 365
print("%d ano(s)" % a)
id = id % 365
m = id / 30
print("%d mes(es)" % m)
d = id % 30
print("%d dia(s)" % d)