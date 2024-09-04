import random

def sorteio_ordem(nomes):
    if not nomes:
        print("A lista de participantes está vazia.")
        return None
    random.shuffle(nomes) 
    return nomes

nomes = []

while True:
    nome = input("Digite o nome do participante (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)

ordem = sorteio_ordem(nomes)

if ordem:
    print("\nOrdem de contemplação:")
    for i, nome in enumerate(ordem, start=1):
        print(f"{i}. {nome}")
