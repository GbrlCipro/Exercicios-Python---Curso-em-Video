# Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo, qual é o nome do homem mais velho, e quantas mulheres tem menos de 21 anos.


idade_total = 0
qtd_homem = 0
qtd_idade = 0
mulher_maior21= 0
idade_homem = 0
hmaisvelho = ""
lista_sexo = ['M', 'F']

for c in range(1,3):
    print('\n')
    print('=' * 30)

    while True:
        nome = input('Nome: ')
        if nome.isalpha():
            break
        else:
            print('Essa opção aceita apenas letras. Digite corretamente.')
    
    while True:
        entrada = input('Idade: ')
        if entrada.isdigit():
            idade = int(entrada)
            idade_total += idade
            qtd_idade +=1 
            break
        else:
            print('Essa opção aceita apenas números. Digite corretamente.')

    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in lista_sexo:
            if sexo == 'M':
                qtd_homem += 1
                if idade > idade_homem:
                    hmaisvelho = nome
                    idade_homem = idade
            else:
                if idade >= 21:
                    mulher_maior21 += 1
            break
        else:
            print('Essa opção aceita apenas os valores "M" para MASCULINO ou "F" para FEMNINO. Digite corretamente.')
            
if qtd_idade != 0:
    media_idade = idade_total / qtd_idade
else:
    media_idade = 0

print('\n')
print('A média de idade do grupo é ->', media_idade, 'anos')

print('Quantidade de mulheres com mais de 21 anos -> ', mulher_maior21)

if mulher_maior21 > 0:
    print('Quantidade de mulheres com mais de 21 anos -> ', mulher_maior21)
else:
    print('Não temos mulheres cadastradas')

if hmaisvelho != '':
    print('O nome do homem mais velho é -> ', hmaisvelho,'e ele tem', idade_homem, ' anos')
else:
    print('Não temos homens cadastrados')

