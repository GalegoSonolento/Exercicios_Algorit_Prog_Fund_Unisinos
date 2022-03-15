# Crie um programa que imprime os números primos entre 0 e 200,
# imprimindo ao final a soma destes números.

iniciar = input('Digite algo para iniciar: ')
i = 0
num = 2
soma = 0

while i < 200:
    isPrimo = True
    cont = 2
    while cont < num:
        if num % cont == 0:
            isPrimo = False
        cont += 1
    if isPrimo:
        print(num)
        soma += num
        i += 1
        num += 1
    else:
        i += 1
        num += 1

print('A soma de todos os primos até 200 é {}'.format(soma))
# while i < 200:
#     primo = True
#     for p in range(2, 200):
#         if i % p == 0:
#             primo = False
#             break
#     if primo:
#         print(i)
#         soma += i
#         i += 1
#         print(i)
# print(soma)