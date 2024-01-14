# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada

from random import shuffle

a1 = str(input('1º aluno: '))
a2 = str(input('2º aluno: '))
a3 = str(input('3º aluno: '))
a4 = str(input('4ºaluno: '))
alunos = [a1,a2,a3,a4]
print('Candidatos: ',alunos)
sequencia_sorteada = shuffle(alunos)
print('A ordem de apresentação deverá ser',(alunos))
