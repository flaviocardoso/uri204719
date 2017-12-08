#Soma de vários valores

N = input()

numArray = map(int, input().split())

sum_integer = 0

if(int(N) >= 1 and int(N) <= 100):
	for num in numArray:
		sum_integer += num

print(sum_integer)