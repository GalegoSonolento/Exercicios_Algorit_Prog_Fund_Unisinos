#  Crie um programa que diga se o número informado pelo usuário é primo ou não.
# Como fazer usando while

num = int(input('Digite um número inteiro qualquer: '))

if num == 0:
    print('Número zero não é primo')
elif num == 1 or num == -1:
    print('1 ou -1 não são primos')
elif num == 2 or num == -2:
    print('Número 2 é primo')
elif num % 2 == 0:
    print('ùnico par primo é 2 \n {} não é primo'.format(num))
elif num == 3 or num == -3:
    print('{} é primo'.format(num))
elif num % 3 == 0:
    print('{} não é primo'.format(num))
elif num == 5 or num == -5:
    print('{} é primo'.format(num))
elif num % 5 == 0:
    print('{} não é primo'.format(num))
elif num == 7 or num == -7:
    print('{} é primo'.format(num))
elif num % 7 == 0:
    print('{} não é primo'.format(num))
elif num == 11 or num == -11:
    print('{} é primo'.format(num))
elif num % 11 == 0:
    print('{} não é primo'.format(num))
elif num == 13 or num == -13:
    print('{} não é primo'.format(num))
elif num % 13 == 0:
    print('{} não é primo'.format(num))
else:
    print('O número é primo')