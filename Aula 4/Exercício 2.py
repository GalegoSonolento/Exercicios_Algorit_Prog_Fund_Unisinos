print('Isso aqui vai analisar qual dos dois números digitados a seguir será maior.')

num1 = int(input('Digite seu primeiro valor (A): '))
num2 = int(input('Digite seu segundo valor (B): '))

if num1 > num2:
    print('O valor \"A" é maior que \"B"!')
elif num1 < num2:
    print('O valor \"B" é maior que \"A"!')
else:
    print('Seus valores são iguais!')