# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o maior e o menor valor que estão na tupla.

import random as rd
import tkinter as tk

def gerarLista():
    tp = tuple(rd.randint(0,100) for _ in range(0,5))
    menor=min(tp)
    maior=max(tp)
    resultado.config(text=f'Lista de números:\n{tp}\nMenor: {menor}\nMaior: {maior}')

root=tk.Tk()
rotulo=tk.Label(root, text='Gerando numeros e verificando o maior e o menor')
rotulo.pack(padx=2, pady=2)
botao=tk.Button(root, text='Clique aqui', command=gerarLista)
botao.pack(padx=2, pady=2)
resultado=tk.Label(root, text='resultado')
resultado.pack(padx=2, pady=2)

root.mainloop()