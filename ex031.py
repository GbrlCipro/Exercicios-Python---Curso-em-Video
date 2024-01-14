
# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrano R$ 0,50 por km para viagens de até 200km
# e R$ 0,45 para viagens mais longas

dist = float(input('Qual é a distância da viagem em km? '))
valor1 = float(0.5)
valor2 = float(0.45)

if dist <= 200:
    print(f'A passagem para sua viagem custa R$ {(dist * valor1):.2f}')
else:
    print(f'A passagem para sua viagem custa R$ {(dist * valor2):.2f}')