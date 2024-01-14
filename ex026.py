
'''
Crie um programa que leia uma frase, e diga:

- Quantas vezes aparece a letra A;
- Em que posição ela aparece pela primeira vez;
- Em que posição ela aparece pela última vez.
'''

frase = str(input('Digite uma frase: ')).lower().strip()
print(f'Na frase: {frase}')

qtd_a = frase.count('a')
posi_a = frase.find('a')
posf_a = frase.rfind('a') # procura determinado caractere partido do lado direito da string

print('A letra "A" aparece {} vezes.'.format(qtd_a))
print('A primeira letra "A" aparece na posição {}'.format(posi_a))
print('A última letra "A" aparece na posição {}'.format(posf_a))


# Codigo Guanabara

'''frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}.'.format(frase.rfind('A')+1))'''
