firstNumber = float(input('Digite um número: '))
secondNumber = float(input('Digite um número: '))
thirdNumber = float(input('Digite um número: '))

if firstNumber > secondNumber > thirdNumber:
  print(firstNumber, secondNumber, thirdNumber)
elif firstNumber > thirdNumber > secondNumber:
  print(firstNumber, thirdNumber, secondNumber)
elif secondNumber > firstNumber > thirdNumber:
  print(secondNumber, firstNumber, thirdNumber)
elif secondNumber > thirdNumber > firstNumber:
  print(secondNumber, thirdNumber, firstNumber)
elif thirdNumber > firstNumber > secondNumber:
  print(thirdNumber, firstNumber, secondNumber)
elif thirdNumber > secondNumber > firstNumber:
  print(thirdNumber, secondNumber, firstNumber)