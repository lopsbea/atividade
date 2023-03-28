number = int(input('Digite um número: '))

fatorial = 1

print(f'{number}! = ', end='')
for i in range(number, 0, -1):
  fatorial = fatorial * i
  if i == 1:
    print(f'1 = {fatorial}')
  else:
    print(f'{i} * ', end='')