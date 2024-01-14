
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 - Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30 - Sobrepeso;
# 30 a 40 - Obesidade;
# Acima de 40 - Obesidade mórbida

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = (peso / (altura * altura))

print(f'\nSeu peso é {peso:.1f} kg\nSua altura é {altura:.2f} m\nIMC: {imc:.1f}\n')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Seu peso está ideal.')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida, se cuide!')