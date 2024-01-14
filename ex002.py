# Faça o programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

nome = input("\033[1;47mDigite seu nome:")
print("É um prazer te conhecer, {}{}!{}".format('\033[1m',nome,'\033[m'))
# print("É um prazer te conhecer, ", nome)
