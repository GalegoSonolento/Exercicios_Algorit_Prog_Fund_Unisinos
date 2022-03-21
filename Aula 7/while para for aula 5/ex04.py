# Crie um programa que imprime os números de 0 a 1000
# em ordem decrescente (ou seja, de 1000 a 0).

iniciar = input('Digite algo para iniciar a contagem: ')
i = 1000
for n in range(0, 1000):
    print(i)
    i -= 1
