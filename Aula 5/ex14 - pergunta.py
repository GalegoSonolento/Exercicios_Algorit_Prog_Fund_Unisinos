#  Crie um programa que diga se o número informado pelo usuário é primo ou não.
# Como fazer usando while

# num = int(input('Digite um número inteiro qualquer: '))
# isPrimo = True
# cont = 2
# while cont < num:
#     if num % cont == 0:
#         isPrimo = False
#         break
#     cont += 1
# if isPrimo:
#     print('É primo!')
# else:
#     print('Não é primo!')

num = int(input('Digite um número qualquer: '))
isPrimo = True
cont = 2
while cont < num:
    if num % cont == 0:
        isPrimo = False
    cont += 1
if isPrimo:
    print('É primo')
else:
    print('Não é primo')