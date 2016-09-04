'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baix,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos
clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser
dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser
informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes.
'''

altura = eval(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))
codigo = int(input("Digite seu código: "))
sair = int(input("Digite (1) continuar ou (0) sair: "))
print("")

maiorAltura = altura
maiorAlturaCodigo = codigo
menorAltura = altura
menorAlturaCodigo = codigo
maiorPeso = peso
maiorPesoCodigo = codigo
menorPeso = peso
menorPesoCodigo = codigo
somaAltura = altura
somaPeso = peso
mediaPeso = 0
mediaAltura = 0
a = 0

while (sair != 0):
	altura = eval(input("Digite sua altura: "))
	peso = int(input("Digite seu peso: "))
	codigo = int(input("Digite seu codigo: "))
	sair = int(input("Digite (1) continuar ou (0) sair: "))	
	print("")
	
	if (altura > maiorAltura):
		maiorAltura = altura
		maiorAlturaCodigo = codigo 
	else:
		maiorAltura = maiorAltura

	if (altura < menorAltura):
		menorAltura = altura
		menorAlturaCodigo = codigo
	else:
		menorAltura =  menorAltura

	if (peso > maiorPeso):
		maiorPeso = peso
		maiorPesoCodigo = codigo
	else:
		maiorPeso = maiorPeso

	if (peso < menorPeso):
		menorPeso = peso
		menorPesoCodigo = codigo
	else:
		menorPeso = menorPeso

	somaAltura = somaAltura + altura
	somaPeso = somaPeso + peso
	a = a + 1

if (a != 0):
	mediaPeso = float(somaPeso) / (a + 1)
	mediaAltura = float(somaAltura) / (a + 1)
	print("O mais magro pesa: %d Kg \n código: %d" % (menorPeso, menorPesoCodigo))
	print("O mais gordo pesa: %d kg \n código: %d" % (maiorPeso, maiorPesoCodigo))
	print("Tamanho do mais baixo: %.2f \n código: %d" % (menorAltura, menorAlturaCodigo))
	print("Tamanho do mais alto: %.2f \n código: %d" % (maiorAltura, maiorAlturaCodigo))
	print("")
	print("Média Peso: %d Kg" % mediaPeso)
	print("Média altura: %.2f metros" % mediaAltura)

