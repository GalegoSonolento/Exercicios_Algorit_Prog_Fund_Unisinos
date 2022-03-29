# Exercício 12. Crie um programa que pede para o usuário digitar números positivos via Teclado.
# Quando o usuário digitar um número negativo, informe a média de todos os números que ele informou.
soma = 0
media = 0
p = 10
for i in range(0, p):
    p += 1
    num = float(input('Digite um valor pelo teclado: '))
    if num >= 0:
        soma += num
    elif num < 0:
        media = soma/2
        print(media)
        break
