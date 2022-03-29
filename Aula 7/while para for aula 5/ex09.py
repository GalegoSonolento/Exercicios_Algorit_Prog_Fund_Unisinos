# Exercício 9. Crie um programa que pede para o usuário digitar 2 valores inteiros via Teclado (val1 e val2).
# Se nenhum dos valores for negativo, escreva os números pares entre o menor e o maior valor.
val1 = int(input('Digite um número inteiro: '))
val2 = int(input('Digite outro: '))
if val1 > 0 and val2 > 0:
    if val1 > val2:
        for i in range(val2 + 1, val1):
            if i % 2 == 0:
                print(i)
    elif val1 < val2:
        for p in range(val1 + 1, val2):
            if p % 2 == 0:
                print(p)
