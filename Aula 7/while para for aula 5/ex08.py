# Exercício 8. Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar
# e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros,
# e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.
quant = int(input('quantos números irá digitar? '))
for p in range(0, quant):
    num = float(input('Digite o número: '))
    if num < 0:
        print('Número negativo')
    elif num == 0:
        print('zero')
    elif num > 0:
        print('Número positivo')
