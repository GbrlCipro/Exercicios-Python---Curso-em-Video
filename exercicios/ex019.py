# Um professor quer sortear um de seus 4 alunos pra apagar o quadro
# Faça um programa que ajude-o, lendo o nome dos alunos, e mostrando
# o escolhido

# Meu método

import random

Alunos = ['joao','jose','maria','pedro']

print(random.choice(Alunos))

# Método Guanabara

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceito aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')
