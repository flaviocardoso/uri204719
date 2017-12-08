#sortsimples.py

vetor = list(map(int, input().split()))

vetor_order = sorted(list(set(vetor)))

for x in vetor_order:
	print(x)
print()
for y in vetor:
	print(y)