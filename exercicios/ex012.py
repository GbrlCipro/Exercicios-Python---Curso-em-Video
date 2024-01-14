# Faça um algoritimo que leia o preço de um produto, e mostre seu novo preço
# com 5% de desconto

v1 = float(input('Qual o valor do produto? '))
d = float(input('Qual o percentual do desconto? '))
print(f'Preço SEM desconto: {v1:.2f}\nValor do desconto (%): {d:.2f}\nPreço COM desconto: {v1-(v1/100*d):.2f}')
