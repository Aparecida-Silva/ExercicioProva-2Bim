'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a
turma é jovem, adulta ou idosa, conforme a média calculada. 
'''

Npessoa = int(input("Digite um número de pessoas: "))

a = 0
soma = 0

while (a < Npessoa):
	idade = int(input("Digite uma idade: "))
	soma = soma + idade
	a = a + 1
media = soma / a
print("")
print("A média é:", media, "anos")

if (media > 0 and media <= 26):
	print("Turma Jovem!")
elif (media > 26 and media <= 60):
	print("Turma Adulta!")
else:
	print("Turma Idosa!")
