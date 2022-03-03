print('Identificação se o número é par ou ímpar utilizando apenas números inteiros')

num = int(input('Digite o número inteiro a ser analisado: '))

teste = num%2

if teste == 0:
    print('Seu número é par!')
else:
    print('Seu número é ímpar!')