'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do
aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais
baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''

a = 0
b = 0
maiorAluno = 0
menorAluno = 1000

for i in range(1, 11):
    num = int(input("Digite o número do aluno: "))
    altura = eval(input("Digite a altura do aluno em centímetros: "))
    print("")
    
    if (altura > maiorAluno):
        maiorAluno = altura
        a = num
    if (altura < menorAluno):
        menorAluno = altura
        b = num
        
print("Número do aluno mais alto é: ", b, "\nO mais alto tem: ", maiorAluno, "centímetros")
print("Número do aluno mais baixo é:", a, "\nO mais baixo tem: ", menorAluno, "centímetros")
