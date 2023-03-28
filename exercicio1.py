firstNum = int(input('A: '))
secondNum = int(input('B: '))
thirdNum = int(input('C: '))

sum = firstNum + secondNum

if sum < thirdNum:
  print(f'A soma dos dois primeiros é menor que {thirdNum}')
elif sum > thirdNum:
  print(f'A soma dos dois primeiros é maior que {thirdNum}')
else:
  print(f'A soma dos dois primeiros é igual a {thirdNum}')