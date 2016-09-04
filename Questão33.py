'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um
conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas
informadas, bem como a média das temperaturas.
'''

num = int(input("Informe quantas temperaturas são:"))
print("")
temperatura = eval(input("Informe a temperatura:"))
Maior = 0
Menor = temperatura
soma = temperatura

for x in range(1, num):
    temperatura = eval(input("Informe a temperatura: "))
    if (temperatura > Maior):
        Maior = temperatura
    elif (temperatura < Menor):
        Menor = temperatura
    soma += temperatura
    
print("")   
media = soma / num

print("A menor temperatura é: ", Menor)
print("A maior temperatura é: ", Maior)
print("A média das temperaturas é: ", media)
