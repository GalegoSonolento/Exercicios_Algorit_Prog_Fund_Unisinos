# Exercício 7. Crie um programa que solicita para o usuário que ele digite 10 valores inteiros.
# Ao final, imprima a soma de todos os valores digitados.
soma = 0
for i in range(0, 10):
    num = float(input('Digite valores: '))
    soma += num
print(soma)
