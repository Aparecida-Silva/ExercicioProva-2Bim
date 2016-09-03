'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
(divisões) executados. 
'''

num = int(input("Digite um número inteiro: "))
testePrimo = 5
divisao = 0

while (testePrimo < num):
	a = 2
	b = 0
	while (a < testePrimo):
		resto = testePrimo % a
		divisao += 1
		if (resto == 0):
			a = testePrimo
			b = 0
		if (resto != 0):
			a += 1
			b = 1
	if (b == 1):
		print("Número primo:", a)
	testePrimo += 1
print("Divisões:", divisao)
