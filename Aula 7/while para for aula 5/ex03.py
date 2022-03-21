# Crie um programa que imprime os números pares de 0 a 2000.

inicio = input('Digite algo para começar: ')
for n in range(1, 2001):
    if n%2 == 0:
        print(n)