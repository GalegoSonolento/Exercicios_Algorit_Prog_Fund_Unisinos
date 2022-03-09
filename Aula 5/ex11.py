# Exercício 11. Crie um programa que imprima a soma dos valores pares
# e a soma dos valores ímpares entre dois números quaisquer digitados pelo usuário.

n1 = float(input('Digite um valor qualquer: '))
n2 = float(input('Digite outro: '))

menor = n1
maior = n2
somap = 0
somai = 0

if n2 < n1:
    menor = n2
    maior = n1

while menor <= maior:
    if menor%2 == 0:
        # print(menor)
        somap = somap + menor
        menor += 1
    elif menor%2 != 0:
        # print(menor)
        somai = somai+menor
        menor += 1

print(somap)
print(somai)