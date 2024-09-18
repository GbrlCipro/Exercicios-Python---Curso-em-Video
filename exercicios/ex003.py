#Escreva a soma de 2 numeros

#n1 = int (input('Digite o primeiro número:')) #convertendo a variável para o tipo INT
#n2 = int (input('Digite o segundo número:'))
#print('A soma dos dois números digitados é', n1 + n2)


import tkinter as tk    

def soma(event=None):
    """
    Função que calcula a soma dos valores inseridos nos campos de entrada.
    Atualiza o rótulo com o resultado e limpa os campos de entrada.
    
    Argumentos:
    event -- (opcional) Evento que aciona a função. Usado para suporte ao atalho de teclado.
    """
    # Obtém os valores dos campos de entrada e converte para inteiros
    num1 = int(n1.get())
    num2 = int(n2.get())
    # Calcula a soma
    resultado = num1 + num2
    # Atualiza o rótulo `res` para mostrar o resultado
    res.config(text=f'Resultado: {resultado}')
    # Limpa os campos de entrada
    n1.delete(0, 'end')
    n2.delete(0, 'end')

def passarProximoCampo(event):
    """
    Função que move o foco para o próximo campo ou widget ao pressionar 'Enter'.
    
    Argumentos:
    event -- Evento de teclado que aciona a função. Usado para navegação entre campos.
    """
    # Move o foco para o próximo widget
    event.widget.tk_focusNext().focus()
    return 'break'

# Cria a janela principal
root = tk.Tk()

# Rótulo que orienta o usuário
rotulo = tk.Label(root, text='Some os dois valores')
rotulo.pack()

# Campo de entrada para o primeiro número
n1 = tk.Entry(root, width=5)
n1.pack()
n1.bind('<Return>', passarProximoCampo)

# Campo de entrada para o segundo número
n2 = tk.Entry(root, width=5)
n2.pack()
n2.bind('<Return>', passarProximoCampo)

# Botão para calcular a soma
botao = tk.Button(root, text='Somar', command=soma)
botao.pack()

# Rótulo para exibir o resultado
res = tk.Label(root, text='Resultado:')
res.pack()

# Associa o evento de pressionar "Enter" à função `soma`
root.bind('<Return>', soma)

# Inicia o loop principal da interface gráfica
root.mainloop()
