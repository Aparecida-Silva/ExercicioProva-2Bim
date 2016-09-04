'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de
trânsito. Foram obtidos os seguintes dados:
	a.Código da cidade;
	b.Número de veículos de passeio (em 1999);
	c.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
	d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
	e.Qual a média de veículos nas cinco cidades juntas;
	f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

codigoCidade = int(input("Digite o código da cidade: "))
quantVeiculos = int(input("Digite o número de veículos na cidade: "))
quantAcidentes = int(input("Digite o número de acidentes com vitimas da cidade: "))
print("")

indiceAcidente = float(quantAcidentes) / quantVeiculos
maiorIndice = indiceAcidente
maiorIndiceCodigo = codigoCidade
menorIndice = indiceAcidente
menorIndiceCodigo = codigoCidade
soma = quantVeiculos
somaVeiculos2000 = 0
divisorMedia2000 = 1

if (quantVeiculos < 2000):
	somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
	divisorMedia2000 = divisorMedia2000 + 1

a = 1
while (a < 5):
	codigoCidade = int(input("Digite o código da cidade: "))
	quantVeiculos = int(input("Digite o número de veículos na cidade: "))
	quantAcidentes = int(input("Digite o número de acidentes com vítimas da cidade: "))
	print("")
	indiceAcidente = float(quantAcidentes) / quantVeiculos
	soma = soma + quantVeiculos

	if (indiceAcidente > maiorIndice):
		maiorIndice = indiceAcidente
		maiorIndiceCodigo = codigoCidade

	if (indiceAcidente < menorIndice):
		menorIndice = indiceAcidente
		menorIndiceCodigo = codigoCidade

	if (quantVeiculos < 2000):
		somaVeiculos2000 = somaVeiculos2000 + quantAcidentes
		divisorMedia2000 = divisorMedia2000 + 1

	a = a + 1

print("\nMenor índice: %.2f \nCódigo da cidade: %d" % (menorIndice, menorIndiceCodigo))
print("\nMaior índice: %.2f \nCódigo da cidade: %d" % (maiorIndice, maiorIndiceCodigo))
print("Média de veículos nas %d cidades = %d veículos" % (a,(float(soma)/a)))
print("Média de acidentes em cidades com menos de 2000 veículos: %.1f" % (float(somaVeiculos2000)/divisorMedia2000))
