
# Crie um programa que leia duas notas de um aluno e calcule a sua média
# mostrando uma mensagem no final, de acordo com a média atingida
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2) / 2

print('Média:', media)

if media < 5:
    print('REPROVADO - Estude mais!')
elif media < 7:
    print('RECUPERAÇÃO - Com esforço, você ainda pode conseguir!')
else:
    print('APROVADO - Parabéns, te vejo no próximo semestre!')