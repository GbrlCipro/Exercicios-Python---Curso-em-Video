# Faça um programa que mostre na tela uma
# contagem regressiva para o estouro
# de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles

from time import sleep

segundos_contagem = 10 # Quantidade de segundos da contagem regressiva

print(("\nCOMEÇANCO A CONTAGEM REGRESSIVA PARA A VIRADA DE ANO!\n"))
sleep(3)
for c in range(segundos_contagem, 0, -1):
    print(c)
    sleep(1)
print("\nFELIZ ANO NOVO !!")