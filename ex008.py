# Escreva um programa que leia um valor em metros, e o exiba convertido em
# centímetros e milímetros

m = float(input('Digite um valor em metros: '))
print(f'Metros {m:.2f}\nQuilômetros {m/1000}\nHectômetros: {m/100}\nDecâmetros: {m/10:.2f}\nDecímetros: {m*10:.2f}\nCentímetros: {m*100:.2f}\nMilímetros: {m*1000:.2f}')
