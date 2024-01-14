
# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço
# normal e condição de pagamento:
# À vista dinheiro/cheque - 10% de desconto;
# À vista no cartão - 5% de desconto;
# Em até 2x no cartão - Preço normal;
# 3x ou mais - 20% de juros

preco = float(input('Qual é o preço do produto? '))
pagamento = int(input('''Qual é a forma de pagamento?
[1] - À vista em dinheiro ou cheque
[2] - À vista no cartão
[3] - 2 vezes no cartão
[4] - 3 vezes ou mais no cartão\n'''))

if pagamento == 1:
    avistaD = preco - (preco / 100 * 10)
    print(f'O valor à vista é {avistaD}')
elif pagamento == 2:
    avistaC = preco - (preco / 100 * 5)
    print(f'O valor à vista no cartão é {avistaC}')
elif pagamento == 3:
    cartao2x = preco
    print(f'O valor em 2 vezes no cartão é {cartao2x}')
elif pagamento == 4:
    cartao3x = preco + (preco / 100 * 20)
    print(f'O valor em 3 vezes ou mais no cartão é {cartao3x}')
else:
    print('Forma de pagamento errada, reinicie e escolha uma opção válida')
