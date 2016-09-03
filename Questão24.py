'''
Faça um programa que calcule o mostre a média aritmética de N notas.
'''

Nnotas = eval(input("Digite um número de notas: "))
a = 0
soma = 0

while (a < Nnotas):
	nota = eval(input("Digite uma nota: "))
	soma = soma + nota
	a = a + 1
media = soma / a
print("")
print("A média aritmétrica das notas é: ", media)
