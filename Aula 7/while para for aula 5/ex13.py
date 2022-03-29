# Exercício 13. Crie um programa que calcule o fatorial
# de um número informado pelo usuário (não permita números negativos).
num = int(input('Digite um número inteiro para encontrar o fatorial: '))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(fatorial)
