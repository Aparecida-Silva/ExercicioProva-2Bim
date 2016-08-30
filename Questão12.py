'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero
ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''
x = int(input("Informe de qual número você deseja ver a tabuada: "))

if (x >= 1 and x <= 10):
    var = 1
    mult = 0
    while (var <= 10):
        mult = x * var
        print(x, "X", var, "=", mult)
        var = var + 1
else:
    print("O número informado é inválido!")
    print("Por favor, informe um número entre 1 e 10!")
        
