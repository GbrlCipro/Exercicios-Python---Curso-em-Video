
# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento
# Para salários superiores a R$ 1250,00 - Aumento de 10%
# Para salários inferiores o aumento é de 15%

sal = float(input('Qual é o salário do funcionário: '))

if sal >= 1250:
    sal = sal + (sal/100*10)
    print(f'Com um aumento de 10%, o novo salário desse funcionário é R$ {sal:.2f}')
else:
    sal = sal + (sal/100*15)
    print(f'Com um aumento de 15%, o novo salário desse funcionário é R$ {sal:.2f}')