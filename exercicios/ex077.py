# Crie um programa que tenha uma tupla com várias palavras. Depois disso você deve mostrar para cada palavra, quais foram suas vogais

nomes = []
tp=tuple(nomes)

def gravarPlvr():
    n = entr.get()
    nomes.append(n)
    entr.delete(0, 'end')
def getVogais():
    result = ''
    for n in nomes:
        v=[]
        for ltr in n:
            if ltr in 'aeiou':
                v.append(ltr)
        result += f'{n}: {" ".join(v)}\n{tp}\n'
    res.config(text=result)
def test():
    res.config(text=nomes)
def close():
    root.destroy()

import tkinter as tk
root = tk.Tk()
txt1 = tk.Label(root, text='Digite um nome para ver suas vogais')
txt1.pack()
entr = tk.Entry(root)
entr.pack()
btn = tk.Button(root, text='Gravar nome', command=gravarPlvr)
btn.pack()
btn3 = tk.Button(root, text='Mostrar nome', command=test)
btn3.pack()
btn1 = tk.Button(root, text='Resultado', command=getVogais)
btn1.pack()
btn2 = tk.Button(root, text='Fechar', command=close)
btn2.pack()
res = tk.Label(root, text='')
res.pack()

root.mainloop()