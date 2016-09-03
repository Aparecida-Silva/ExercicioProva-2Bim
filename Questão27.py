'''
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade
de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. 
'''

turma = int(input("Digite a quantidade de turmas: "))
print("")
soma = 0

for a in range(1, turma +1):
	alunos = int(input("Digite a quantidade de alunos por turma: "))
	while (alunos > 40):
		print("As turmas não podem ter mais de 40 alunos!")
		alunos = int(input("Digite a quantidade de alunos por turma: "))
	soma = soma + alunos
	a = a + 1
	
print("")	
media = soma / turma	
print("Numero médio de alunos: ", media)

