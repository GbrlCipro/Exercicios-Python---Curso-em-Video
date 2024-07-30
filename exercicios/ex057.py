# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


while True:
    lista_generos = ['M', 'F']
    genero = input('Digite o sexo da pessoa [M/F]: ').upper()[0].strip()
    if genero in lista_generos:
        break
    else:
        print('Dados incorretos. Por favor informe o sexo do paciente.')