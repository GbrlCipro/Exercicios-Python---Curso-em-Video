# Crie um programa que simule o funcinamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

total = int(input("Total R$: "))

# cédulas
n50 = 50
n20 = 20
n10 = 10
n1 = 1

sobra50 = total % n50
sobra20 = sobra50 % n20
sobra10 = sobra20 % n10
sobra1 = sobra10 % n1

qtdNota50 = (total - sobra50) // n50
qtdNota20 = (sobra50 - sobra20) // n20
qtdNota10 = (sobra20 - sobra10) // n10
qtdNota1 = (sobra10 - sobra1) // n1

print(f'\nTotal: R$ {total},00\n')
print(f'Qtd notas R$ 50,00: {qtdNota50}')
print(f'Qtd notas R$ 20,00: {qtdNota20}')
print(f'Qtd notas R$ 10,00: {qtdNota10}')
print(f'Qtd notas R$ 1,00: {qtdNota1}')