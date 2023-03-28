firstNum = int(input('Digite um número inteiro: '))
secondNum = int(input('Digite um número inteiro: '))

if firstNum == secondNum:
  thirdNum = firstNum + secondNum
  print(f'{firstNum} + {secondNum} = {thirdNum}')
else:
  thirdNum = firstNum * secondNum
  print(f'{firstNum} * {secondNum} = {thirdNum}')