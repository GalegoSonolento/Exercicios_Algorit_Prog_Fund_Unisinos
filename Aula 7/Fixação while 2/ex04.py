# Já fiz algo parecido

num1 = int(input('Coloque um número inteiro: '))
num2 = int(input('Coloque outro: '))

if num1 > num2:
    while num1 > num2:
        print(num2)
        num2 += 1

while num1 < num2:
    print(num1)
    num1 += 1