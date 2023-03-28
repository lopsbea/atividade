sex = input('Digite M ou F para seu sexo: ')
height = float(input('Digite sua altura: '))
weight = float(input('Digite seu peso: '))

if sex == 'm' or sex == 'M':
  idealWeight = (72.7 * height) - 58
  print(f'Peso ideal: {idealWeight}kg')
else:
  idealWeight = (62.1 * height) - 44.7
  print(f'Peso ideal: {idealWeight}kg')
  
imc = weight / (height ** 2)

if imc < 18.5:
  print('Abaixo do peso')
elif imc < 25:
  print('Peso normal')
elif imc < 30:
  print('Acima do peso')
else:
  print('Obeso')
