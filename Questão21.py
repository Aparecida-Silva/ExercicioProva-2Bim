'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um
número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

num = int(input("Digite um número inteiro: "))

x = 2
a = 0

while (x < num):
	if (num % x == 0):
		a = 0
		x = num
	else:
		x = x + 1
		a = 1
		
if (a == 1 or num == 2):
	print("O número", num, "é primo!")
	
else:
	print("O número", num, "não é primo!")
