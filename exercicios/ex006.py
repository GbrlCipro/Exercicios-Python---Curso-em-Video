# Crie um algoritimo que leia um número, e mostre o seu dobro, o seu triplo e
# sua raiz quadrada

n = int(input('Digite um número: '))
print('Número digitado: {}\nDobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(n,(n*2),(n*3),pow(n,(1/2))))
