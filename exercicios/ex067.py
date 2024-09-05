# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

'''def tabuada(n):
    multiplicador = n
    multiplicando = 1
    resultado = ''
    while multiplicando <= 10:
        resultado += f'{multiplicador} X {multiplicando} = {multiplicador * multiplicando}\n'
        multiplicando += 1
    #print(resultado)
    return resultado

print(tabuada(1))'''

n = 0
while True:
    n = int(input('Digite o multiplicador: '))
    if n >= 0:
        multiplicador = n
        multiplicando = 1
        resultado = ''
        while multiplicando <= 10:
            resultado += f'{multiplicador} X {multiplicando} = {multiplicador * multiplicando}\n'
            multiplicando += 1
        print(resultado)
    else:
        break