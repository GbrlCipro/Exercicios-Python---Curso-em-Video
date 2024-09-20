# Crie um programa que tenha uma tupla com várias palavras. Depois disso você deve mostrar para cada palavra, quais foram suas vogais

nomes = []

def gravarPlvr():
    n = entr.get()
    nomes.append(n)
    entr.delete(0, 'end')

def vogaisPorPalavra():
    v = []
    for n in nomes:
        for ltr in n:
            if ltr in 'aeiou':
                v.append(ltr)
    res.config(text=f'{n}, {v}') # ESTA TRAZENDO SO O ULTIMO NOME DIGITADO 

def teste():
    res.config(text=nomes)

def close():
    root.destroy()

import tkinter as tk
root = tk.Tk()
txt1 = tk.Label(root, text='texto 1')
txt1.pack()
entr = tk.Entry(root)
entr.pack()
btn = tk.Button(root, text='Gravar', command=gravarPlvr)
btn.pack()
btn1 = tk.Button(root, text='clique', command=vogaisPorPalavra)
btn1.pack()
btn2 = tk.Button(root, text='FECHAR', command=close)
btn2.pack()
btn3 = tk.Button(root, text='imprimir', command=teste)
btn3.pack()
res = tk.Label(root, text='resultado apos o clique')
res.pack()
root.mainloop()