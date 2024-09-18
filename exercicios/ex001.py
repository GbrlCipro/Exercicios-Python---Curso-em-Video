# Crie um programa que escreva "Olá, Mundo!" na tela.

#msg = "\033[0;30;47mOlá, Mundo!\033[m"
#print(msg)

import tkinter as tk

def imprimirtexto(event=None):
    texto = campotxt.get()    
    campotxt.delete(0, 'end')
    msg.config(text=f'Você inseriu: {texto}')

root = tk.Tk()

rotulo = tk.Label(root, text='Digite a mensagem, e clique para retorna-la na janela')
rotulo.pack()

campotxt = tk.Entry(root)
campotxt.pack()

botao = tk.Button(root, text='Clique para imprimir', width=20, command=imprimirtexto)
botao.pack()

msg = tk.Label(root, text='Sua mensagem aparecerá aqui')
msg.pack()

root.bind('<Return>', imprimirtexto)

root.mainloop()