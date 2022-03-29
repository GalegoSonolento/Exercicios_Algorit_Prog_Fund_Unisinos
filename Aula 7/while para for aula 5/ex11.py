# Exercício 11. Crie um programa que imprima a soma dos valores pares
# e a soma dos valores ímpares entre dois números quaisquer digitados pelo usuário.
val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro: '))
somap = 0
somai = 0
if val1 > val2:
    for i in range(val2, val1+1):
        if i % 2 == 0:
            somap += i
        elif i % 2 != 0:
            somai += i
elif val1 < val2:
    for p in range(val1, val2+1):
        if p % 2 == 0:
            somap += p
        elif p % 2 != 0:
            somai += p

print('A soma dos pares é: {}'.format(somap))
print('A soma dos ímpares é: {}'.format(somai))
