#addtwoarrays

N = int(input())

numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

if(N >= 1 and N <= 100):
	for i in range(N):
		sumArray.append(numArray1[i] + numArray2[i])

for element in sumArray:
	print(element, end=" ")