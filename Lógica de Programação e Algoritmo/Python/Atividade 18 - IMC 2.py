peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)

print(f"O IMC dessa pessoa é: {round(imc,2)}")

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso Normal')
elif imc <= 34.9:
    print('Sobrepeso')
elif imc <= 35.9:
    print('Obesidade grau 1')
elif imc <= 39.9:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')