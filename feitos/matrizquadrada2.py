#/usr/bin/python3
#matrizquadrada2.py 1478

n = int(input())

while n != 0:	
	for i in range(n):
		for j in range(n):
			print(abs(j - i) + 1, end=" ")
		print()
	print()

	n = int(input())



'''
  1

  1   2
  2   1

  1   2   3
  2   1   2
  3   2   1

  1   2   3   4
  2   1   2   3
  3   2   1   2
  4   3   2   1

  1   2   3   4   5
  2   1   2   3   4
  3   2   1   2   3
  4   3   2   1   2
  5   4   3   2   1

'''