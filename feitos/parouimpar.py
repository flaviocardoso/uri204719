#!/bin/python3
#uri 1074
N = int(input())

for x in range(N):
   e = int(input())
   if(e == 0):
      print("NULL")
   else:
      if(e > 0):
         if(e%2==0):
            print("EVEN POSITIVE")
         else:
            print("ODD POSITIVE")
      else:
         if(e%2==0):
            print("EVEN NEGATIVE")
         else:
            print("ODD NEGATIVE")
