
# Faça um programa que leia o ano de nascimento de um jovem, e informe de
# acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou o tempo de alistamento
# Seu programa também deverá mostrar o tempo que passou ou que falta para o prazo

idade = int(input('Digite sua idade: '))
idadeAlistamento = 18

if idade > 18:
    diferencaMais = idade - idadeAlistamento
    if diferencaMais == 1:
        print('Seu prazo já passou.')
        print(f'Passou apenas {diferencaMais} ano da sua data de alistamento, talvez ainda consiga resolver essa questão.')
    else:
        print('Seu prazo já passou.')
        print(f'Se passaram {diferencaMais} anos da data em que você precisaria se alistar.')
elif idade < 18:
    diferencaMenos = idadeAlistamento - idade
    if diferencaMenos != 1:
        print('Ainda não chegou o prazo, aguarde mais um pouco.')
        print(f'Faltam {diferencaMenos} anos para se alistar')
    else:
        print(f'Falta apenas {diferencaMenos} ano para seu alistamento.')
else:
    print('Vamos lá, hora de se alistar!')
