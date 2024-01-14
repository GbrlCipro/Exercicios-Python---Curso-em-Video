
# Refaça o desafio dos TRIÂNGULOS 035, acrescentando o recurso de mostrar que tipo
# de triângulo será mostrado:
# Equilátero - Todos os lados iguais;
# Isósceles - Dois lados iguais;
# Escaleno - Lados diferentes

l1 = float(input('Digite  o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os lados acima PODEM formar um triângulo')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Esse é um triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Esse é um triângulo Isóceles')
    else:
        print('Esse é um triângulo Escaleno')
else:
    print('Os lados acima NÃO PODEM formar um triângulo')
