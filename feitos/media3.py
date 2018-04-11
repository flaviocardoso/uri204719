#media3
'''
Leia quatro números (N1, N2, N3, N4),
cada um deles com uma casa decimal,
correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1,
respectivamente, para cada uma destas notas e
mostre esta média acompanhada pela mensagem
"Media: ". Se esta média for maior ou igual a 7.0,
 imprima a mensagem "Aluno aprovado.".
 Se a média calculada for inferior a 5.0,
 imprima a mensagem "Aluno reprovado.".
 Se a média calculada for um valor entre 5.0 e 6.9,
 inclusive estas, o programa deve imprimir a mensagem
 "Aluno em exame.".

No caso do aluno estar em exame,
leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame:
" acompanhada pela nota digitada.
Recalcule a média
(some a pontuação do exame com a média anteriormente calculada e
 divida por 2). e imprima a mensagem "Aluno aprovado."
 (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.",
 (caso a média tenha ficado 4.9 ou menos).
 Para estes dois casos (aprovado ou reprovado após ter pego exame)
 apresente na última linha uma mensagem "Media final: "
 seguido da média final para esse aluno.

entrada
2.0 4.0 7.5 8.0
6.4
saida
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9

entrada
2.0 6.5 4.0 9.0
saida
Media: 4.8
Aluno reprovado.

entrada
9.0 4.0 8.5 9.0
saida
Media: 7.3
Aluno aprovado.
'''

N1, N2, N3, N4 = list(map(float, input().split()))

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

print("Media: {0:.1f}".format(float(media)))

if (media >= 7.0):
	print("Aluno aprovado.")
if (media < 5):
	print("Aluno reprovado.")
if(media >= 5 and media <= 6.9):
	print("Aluno em exame.")
	N5 = float(input())
	print("Nota do exame:", N5)
	Nmedia = (N5 + media)/2
	if ((Nmedia) >= 5):
		print("Aluno aprovado.\nMedia final:", Nmedia)
	else:
		print("Aluno reprovado.")
