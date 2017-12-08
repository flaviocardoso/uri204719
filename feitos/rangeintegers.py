#rangeintegers

L, R = map(int, input().split())
string = ""
for x in range(L, R+1):
	string += str(x) + " "
print(string)