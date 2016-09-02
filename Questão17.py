'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120 
'''

num = int(input("Digite um numero: "))
numCalc = num
fatorial = 1

while (numCalc > 0):
	fatorial = fatorial * numCalc
	numCalc -= 1

print("Fatorial de ", num, "=", fatorial)
