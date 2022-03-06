# Exercício 7. Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano
# informado é bissexto ou não.

print('Insira o ano para avaliação se é bissexto ou não!')

ano = int(input('Insira o ano aqui: '))

if ano%4 == 0:
    print('parabéns! Seu ano é bissexto!')
else:
    print('O ano colocado não é bissexto.')