'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo
usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial
e final devem ser informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''

comeco = 10
final = 1
tabuada = 1

while (comeco >= final):
	tabuada = int(input("Digite a tabuada que deseja (1 a 10): "))
	comeco = int(input("Digite por qual número deseja começar: "))
	final = int(input("Digite por qual número deseja finalizar: "))
	if (comeco >= final):
		print("")
		print("O valor inicial não pode ser maior que o final!\n")
		print("")
		
print("")	
print("Tabuada de: ", tabuada)
print("Inicializada por: ", comeco)
print("Finalizada por: ", final)

while (comeco < (final + 1)):
	print(tabuada, "X", comeco, "=", tabuada * comeco)
	comeco = comeco + 1
