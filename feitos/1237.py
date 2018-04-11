#! /usr/bin/env python3
from sys import stdin

while True:
    try:
        s1 = input()
        s2 = input()

        n = 0
        m = 0
        sa = 0
        sb = 0
        while sa < len(s2):
            while sb < len(s1):
                if (s1[sb] == s2[sa]):
                    n = n + 1
                    sb = sb + 1
                else:
                    break
            sb = 0            
            if (n > m):
                m = n
            n = 0
            sa = sa + 1
        print(m)
    except EOFError:
        break
