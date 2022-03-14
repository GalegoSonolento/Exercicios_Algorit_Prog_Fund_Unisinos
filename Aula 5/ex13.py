# Crie um programa que calcule o fatorial de um número informado pelo
# usuário (não permita números negativos).

num = int(input('Digite um número inteiro (não negativo) para a realização de um fatorial: '))
i = num - 1
n = num

if i > 0:
    while i > 0:
        num *= i
        i -= 1
    print('O fatorial de {} é {}'.format(n, num))
elif i == 0:
    print('Fatorial de {} é 1.'.format(num))
else:
    print('Coloque um número adequado (apenas positivos)')

