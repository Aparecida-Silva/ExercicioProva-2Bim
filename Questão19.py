'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''

N = int(input("Digite uma certa quantidade de números que deseja: "))

x = 1
soma = 1
num = int(input("Digite um número (entre 0 e 1000): "))
MaiorNum = num
MenorNum = num

if (num > 0 and num < 1000):
	while (x < N):
		if (x < N):
			num = int(input("Digite um número (entre 0 e 1000): "))
		if (num > MaiorNum):
			MaiorNum = num
		elif (num < MenorNum):
			MenorNum = num
		soma = soma + num
		x = x + 1

	print("")
	print("O maior valor é: ", MaiorNum)
	print("O menor valor é: ", MenorNum)
	print("A soma dos valores é: ", soma)
	print("Obrigado(a)!")

elif(num < 0):
	print("Este número é menor que 0(zero)!")
	
else:
	print("Este número é maior que 1000(mil)")
