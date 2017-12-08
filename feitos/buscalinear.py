#busca linear

N, M = map(int, input().split())
index = -1
array = list(map(int, input().split()))

if(N >= 1 and N <= 100000 and M >= 1 and M <= 10000000000):
    for i in range(N):
        arraylist = array[i]
        if(arraylist >= 1 and arraylist <= 10000000000):
            if array[i] == M:
                index = (i + 1)

print(index)