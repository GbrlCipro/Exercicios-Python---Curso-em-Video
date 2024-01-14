
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/H, mostre uma mensagem avisando que ele foi multado
# A multa deve custar R$ 7,00 por cada km acima da velocidade limite

vel = float(input('Velocidade aferida: '))
lim = int(80)
min = int(lim//2)

print(f'Sua velocidade é {vel:.0f} km/H, e o limite da via é {lim} Km/H.')

if vel > lim:
    print('Multado em R$ {:.2f}.'.format((vel-lim)*7))
elif vel < (lim//2):
    print('Multado em R$ {:.2f} por dirigir abaixo do limite de velicidade mínimo da via.'.format((min-vel)*7))
else:
    print('Dentro do limite de velocidade')