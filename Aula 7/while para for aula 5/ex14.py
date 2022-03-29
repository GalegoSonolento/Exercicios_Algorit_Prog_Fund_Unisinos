# Exercício 14.
# Crie um programa que diga se o número informado pelo usuário é primo ou não.
num = int(input('Digite um número inteiro: '))
isPrimo = True
for i in range(2, num):
    if num % i == 0:
        isPrimo = False
if isPrimo:
    print('Seu número é primo')
else:
    print('Seu número não é primo')
