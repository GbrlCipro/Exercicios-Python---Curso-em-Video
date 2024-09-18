# Faça o programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

#nome = input("\033[1;47mDigite seu nome:")
#print("É um prazer te conhecer, {}{}!{}".format('\033[1m',nome,'\033[m'))
# print("É um prazer te conhecer, ", nome)

import tkinter as tk

# Função que será chamada quando o botão for clicado ou a tecla Enter for pressionada
def imprimirtexto(event=None):
    # Obtém o texto inserido no campo de entrada
    texto = campotxt.get()
    # Limpa o campo de entrada
    campotxt.delete(0, 'end')
    # Atualiza o rótulo `msg` para exibir uma mensagem personalizada
    msg.config(text=f'É um prazer te conhecer {texto}!')

# Cria a janela principal da aplicação
root = tk.Tk()

# Cria um rótulo (Label) com a pergunta "Qual é o seu nome?" e o adiciona à janela
rotulo = tk.Label(root, text='Qual é o seu nome?')
rotulo.pack()  # Exibe o rótulo na janela

# Cria um campo de entrada (Entry) onde o usuário pode digitar seu nome
campotxt = tk.Entry(root)
campotxt.pack()  # Exibe o campo de entrada na janela

# Cria um botão (Button) que, ao ser clicado, chama a função `imprimirtexto`
botao = tk.Button(root, text='Salvar', width=20, command=imprimirtexto)
botao.pack()  # Exibe o botão na janela

# Cria um rótulo (Label) vazio que será usado para exibir a mensagem final
msg = tk.Label(root, text='')
msg.pack()  # Exibe o rótulo na janela

# Configura o evento de pressionar a tecla "Enter" para chamar a função `imprimirtexto`
root.bind('<Return>', imprimirtexto)

# Inicia o loop principal da aplicação, exibindo a janela e aguardando interações do usuário
root.mainloop()
