# Escreva um programa que pergunte a quantidade de quilômetros percorridos
# por um carro, e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$
# 0,15 por km rodado

d = int(input('Por quantos dias o carro ficou alugado? '))
valor_d = 60
tot_vd = d * valor_d
km_r = float(input('Quantos quilômetros foram rodados? '))
valor_km = 0.15
tot_kmr = km_r * valor_km
print(f'Diárias do aluguel: {d} = R$ {tot_vd:.2f}\nQuilômetros rodados: {km_r:.2f} = R$ {tot_kmr:.2f}\nTotal a pagar: R$ {tot_vd + tot_kmr:.2f}')
