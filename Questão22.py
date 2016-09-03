'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
'''

num = int(input("Digite um número inteiro: "))

x = 1
a = 0
b = 0

while (x <= num):
  resultado = num / x
  if (resultado == int(resultado)):
    print("É divisível por", x)
    a = a + 1
  else:
    b = b + 1
  x = x + 1
  
if (a == 1 or num == 2):
	print("O número", num, "é primo!")
	
else:
	print("O número", num, "não é primo!")
