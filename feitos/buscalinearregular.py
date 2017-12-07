#buscalinearregular

N = int(input())
vetor = list()

for a in range(N):
	S = input()
	c = 0
	for l in S:
		if l in "aeiouAEIOU":
			c = c + 1
	vetor.append(c)
	#print(c)

for x in vetor:
	print(x)