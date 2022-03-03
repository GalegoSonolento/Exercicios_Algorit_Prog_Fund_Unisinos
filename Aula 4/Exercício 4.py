print('Identificar qual dos 3 valores é menor:')

num1 = int(input('valor A: '))
num2 = int(input('Valor B: '))
num3 = int(input('Valor C: '))

if num1 < num2 and num1 < num3:
    print('Valor A é o menor!')
elif num2 < num1 and num2 < num3:
    print('Valor B é o menor!')
elif num3 < num1 and num3 < num2:
    print('Valor C é o menor!')