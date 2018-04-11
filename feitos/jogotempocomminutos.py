#!/bin/python3
#uri 1047
#tempo de jogo com minutos
'''
7 8 9 10  - O JOGO DUROU 2 HORA(S) E 2 MINUTOS
7 7 7 7 - O JOGO DUROU 24 HORA(S) E 0 MINUTOS
7 10 8 9 - O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
'''

HI, MI, HF, MF = map(int, input().split())

DH = HF - HI
DM = MF - MI

if(HF <= HI):
    DH = 24 + DH
if(MF < MI):
    DM = 60 + DM
    DH = DH - 1
print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(DH, DM))
