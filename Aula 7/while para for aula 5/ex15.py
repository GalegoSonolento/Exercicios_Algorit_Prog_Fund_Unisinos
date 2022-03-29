# Exercício 15.
# Crie um programa que imprime os números primos entre 0 e 200,
# imprimindo ao final a soma destes números.
input('Digite algo para iniciar a contagem: ')
soma = 0
for i in range(1, 201):
    isPrimo = True
    for p in range(2, i):
        if i % p == 0:
            isPrimo = False
    if isPrimo:
        print(i)
        soma += i
print(soma)
