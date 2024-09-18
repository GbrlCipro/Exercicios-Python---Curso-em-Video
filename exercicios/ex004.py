# Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

#a: str = input('Digite algo: ')

#print('O tipo primitivo desse valor é {}'.format(type(a)))
#print('É um número? {}'.format(a.isnumeric()))
#print('É alfa-numérico? {}'.format(a.isalnum()))
#print('É alfabético? ', a.isalpha())
#print('É ASCII? ', a.isascii())
#print('É dígito? ', a.isdigit())
#print('É decimal? ', a.isdecimal())
#print('É identificador? ', a.isidentifier())
#print('É minúsculo? ', a.islower())
#print('É imprimível? ', a.isprintable())
#print('É composto somente por espaços? ', a.isspace())
#print('Está capitalizada? (primeira letra em maiúsculo) ', a.istitle())
#print('É maiúsculo? ', a.isupper())

import tkinter as tk

def mostrar_info():
    # Obtém o valor do campo de entrada
    texto = entrada.get()
    
    # Coleta informações sobre o texto
    info = []
    info.append(f'O tipo primitivo desse valor é {type(texto).__name__}')
    info.append(f'É um número? {texto.isnumeric()}')
    info.append(f'É alfa-numérico? {texto.isalnum()}')
    info.append(f'É alfabético? {texto.isalpha()}')
    info.append(f'É ASCII? {texto.isascii()}')
    info.append(f'É dígito? {texto.isdigit()}')
    info.append(f'É decimal? {texto.isdecimal()}')
    info.append(f'É identificador? {texto.isidentifier()}')
    info.append(f'É minúsculo? {texto.islower()}')
    info.append(f'É imprimível? {texto.isprintable()}')
    info.append(f'É composto somente por espaços? {texto.isspace()}')
    info.append(f'Está capitalizada? (primeira letra em maiúsculo) {texto.istitle()}')
    info.append(f'É maiúsculo? {texto.isupper()}')
    
    # Atualiza o rótulo com as informações coletadas
    resultado.config(state=tk.NORMAL)
    resultado.delete(1.0, tk.END)  # Limpa o conteúdo anterior
    resultado.insert(tk.END, '\n'.join(info))
    resultado.config(state=tk.DISABLED)

# Cria a janela principal
root = tk.Tk()
root.title("Analisador de Texto")

# Rótulo e campo de entrada
rotulo = tk.Label(root, text='Digite algo:')
rotulo.pack(padx=10, pady=5)

entrada = tk.Entry(root, width=50)
entrada.pack(padx=10, pady=5)

# Botão para processar o texto
botao = tk.Button(root, text='Mostrar Informações', command=mostrar_info)
botao.pack(padx=10, pady=5)

# Área de texto para exibir informações
resultado = tk.Text(root, height=15, width=60, wrap=tk.WORD, state=tk.DISABLED)
resultado.pack(padx=10, pady=5)

# Inicia o loop principal da interface gráfica
root.mainloop()
