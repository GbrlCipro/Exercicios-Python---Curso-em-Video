
# Escreva um programa para aprovar um empréstimo de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador,
# e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário, ou então o empréstimo será negado

vcasa = int(input('Qual é o valor do imóvel? '))                 # valor da casa
sal = int(input('Qual é o salario do comprador? '))                     # salário do comprador
prazoAnos = int(input('Qual é o prazo do financiamento? (em anos) ')) * 12           # prazo do financiamento (em anos)
#prazoMeses = int(prazoAnos * 12)    # prazo do financiamento (em meses)
mens = vcasa / prazoAnos          # valor da mensalidade

print(f'Valor da casa: {vcasa:.2f} reais')
print(f'Prazo do financiamento: {prazoAnos} meses')
print(f'Renda do comprador: {sal:.2f} reais')
print(f'Valor da mensalidade: {mens:.2f} reais')

if mens > (sal/100*30):             # SE o valor da mensalidade for MAIOR que 30% da renda do comprador ->
    print('Financiamento REPROVADO pois a parcela do imóvel excedeu 30% da renda do comprador.')
else:                               # SE NÃO for maior ->
    print('Financiamento APROVADO, PARABÉNS!!')
