# Pedir pro usuário colocar 2 valores, o primeiro deve ser menor que o segundo, caso contrário, tem q imprimir uma
# mensagem de erro
# Tem que ter a comparação dos dois números dentro de um while que vai imprimir todos o números ao mesmo tempo

num1 = int(input('Coloque um número inteiro: '))
num2 = int(input('Coloque outro: '))

if num2 < num1:
    print('Erro, o primeiro número deve ser menor que o segundo')

while num1 < num2 - 1:
    num1 += 1
    print(num1)