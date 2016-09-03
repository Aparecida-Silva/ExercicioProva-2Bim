'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor
e a soma dos valores. 
'''

N = int(input("Digite uma certa quantidade de números que deseja: "))

x = 1
soma = 1
num = eval(input("Digite um número: "))
MaiorNum = num
MenorNum = num

while (x < N):
    if (x < N):
        num = eval(input("Digite um número: "))
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
