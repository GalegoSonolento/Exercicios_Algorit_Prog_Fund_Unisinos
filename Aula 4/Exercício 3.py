print('Digitar 2 valores para identificação da divisão.')

num1 = int(input('Valor de A: '))
num2 = int(input('Valor de B:'))

if num2 == 0:
    print('Impossível realizar uma divisão por zero, tente outro número')
    num2 = int(input('Valor de B: '))

print('Sua divisão é: ', num1/num2)