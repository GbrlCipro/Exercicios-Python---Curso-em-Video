# Faça um algoritimo que leia o salário de um funcionário, e mostre seu novo
# salário, com aumento de 15%.

s = float(input('Digite o salário atual: '))
a = 15
print(f'Com um aumento de {a}%, o salário do funcionário passa de R$ {s:.2f} para R$ {s+(s/100*a):.2f}.')
