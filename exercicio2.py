name = input('Digite seu nome: ')
sex = input('Digite seu sexo: ')
status = input('Digite seu estado civil: ')

options = ['m', 'M', 'f', 'F']

if sex not in options:
  print('Por favor, digite F ou M para seu sexo')
  
if status.lower() == 'casada' or status.upper() == 'casado':
  time = input('Quantos anos de casamento? ')
  partner = input('Qual o nome de seu(sua) companheiro(a)? ')
  print(partner)
  print(name)
  print(f'Casados há {time} ano(s)')
