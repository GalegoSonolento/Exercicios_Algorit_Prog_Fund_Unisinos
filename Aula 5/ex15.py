# Crie um programa que imprime os números primos entre 0 e 200,
# imprimindo ao final a soma destes números.

iniciar = input('Digite algo para iniciar: ')
i = 0
n = 0
soma = 0

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

while i < 200:
    if n == 0:
        i += 1
        n += 1
    elif n == 1:
        i += 1
        n += 1
    elif n == 2:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 2 == 0:
        i += 1
        n += 1
    elif n == 3:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 3 == 0:
        i += 1
        n += 1
    elif n == 5:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 5 == 0:
        i += 1
        n += 1
    elif n == 7:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 7 == 0:
        i += 1
        n += 1
    elif n == 11:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 11 == 0:
        i += 1
        n += 1
    elif n == 13:
        print(n)
        soma += n
        i += 1
        n += 1
    elif n % 13 == 0:
        i += 1
        n += 1
    else:
        print(n)
        soma += n
        i += 1
        n += 1

print(soma)