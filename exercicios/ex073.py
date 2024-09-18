# Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados;
# B) Os 4 últimos colocados;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição da tabela está o time Chapecoense.

times = ('São Paulo', 'Botafogo', 'Palmeiras', 'Flamengo', 'Corinthias', 'Goiás', 'Vila Nova', 'Chapecoense', 'Independente RV', 'Bragantino', 'Santos', 'Vasco', 'America de Minas', 'Fluminese', 'Paysandu', 'Real Madrid', 'Barcelona', 'Milan', 'Arsenal', 'PSG')

lista=list(times)
lista.sort()

top5 = times[:5]
down4 = times[-4:]
posChap = times.index('Chapecoense')+1

import tkinter as tk

root = tk.Tk()

timesFormatado = ', '.join(times)
listaFormatada=', '.join(lista)
top5Formatado=', '.join(top5)
down4Formatado=', '.join(down4)

rotulo1 = tk.Label(root, text=f'Times do campeonato Brasileiro 2024 (Ordem de colocação)\n{timesFormatado}')
rotulo1.pack(pady=2)

rotulo3 = tk.Label(root, text=f'Os 5 primeiros colocados do campeonato:\n{top5Formatado}')
rotulo3.pack(pady=2)

rotulo5 = tk.Label(root, text=f'Os 4 últimos colocados do campeonato:\n{down4Formatado}')
rotulo5.pack(pady=2)

rotulo9 = tk.Label(root, text=f'Classificação do Chapecoense:\n{posChap}ª posição')
rotulo9.pack(pady=2)

rotulo11= tk.Label(root, text=f'Times em ordem alfabética:\n{listaFormatada}')
rotulo11.pack(pady=2)

root.mainloop()