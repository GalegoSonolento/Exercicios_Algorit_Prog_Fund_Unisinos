print('Digite dois valores, caso nenhum for negativo, os pares entre eles aparecerão na tela.')

val1 = int(input('Digite o valor 1: '))
val2 = int(input('Digite o valor 2: '))
pares = 'Os números pares entre os digitados são: '

if val1 < 0 and val2 < 0:
    print('Ambos são negativos')
elif val1 < 0:
    print('Valor 1 é negativo')
elif val2 < 0:
    print('Valor 2 é negativo')
else:
    menor = val1
    maior = val2

    if val2 < val1:
        menor = val2
        maior = val1

    while menor < maior:
        if menor%2 == 0:
            print(menor)
        menor += 1
