'''
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números
primos existentes entre 1 e um número inteiro informado pelo usuário.
'''

num = int(input("Digite um número inteiro: "))

print(1)
print(2)
print(3)
testePrimo = 5

while (testePrimo < num):
	a = 2
	b = 0
	while (a < testePrimo):
		resto = testePrimo % a
		if (resto == 0):
			a = testePrimo
			b = 0
		if (resto != 0):
			a = a + 1
			b = 1
	if (b == 1):
		print(a)
	testePrimo = testePrimo + 1
