# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tp = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

ent = int(input())
indx = tp.index('tres')+1

extn = ''

for n in tp:
    if ent == indx:
        extn = tp[ent-1]

print(extn, ent)

# def close(): # função para fechar a janela do programa
#     root.destroy()

# import tkinter as tk

# root = tk.Tk()

# txt = tk.Label(root, text='')
# txt.pack()

# entr = tk.Entry(root)
# entr.pack()

# btn = tk.Button(root, text='')
# btn.pack()

# buttonClose = tk.Button(root, text='', command=close)
# buttonClose.pack()

# res = tk.Label(root, text='')
# res.pack()

# root.mainloop()