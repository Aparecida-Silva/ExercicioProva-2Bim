'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitor.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. 
'''

Neleitores = int(input("Digite o numero de eleitores: "))
print("")

a = 0
soma1 = 0
soma2 = 0
soma3 = 0

while (a < Neleitores):
	print("Você vota para qual candidato? ")
	voto = int(input("Digite:\n(1) Candidato 1\n(2) Candidato 2\n(3) Candidato 3\n "))
	if (voto == 1):
		soma1 += 1
	elif (voto == 2):
		soma2 += 1
	elif (voto == 3):
		soma3 += 1
	a += 1

print("NÚmero de votos do Candidato 1: ", soma1)
print("Número de votos do Candidato 2: ", soma2)
print("Número de votos do Candidato 3: ", soma3)
