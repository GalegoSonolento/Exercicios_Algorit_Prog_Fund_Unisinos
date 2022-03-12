print('Informe apenas números positivos')

num = float(input('Informe os números: '))
base = 0
i = num
p = 1
f = 0
f += 1

while num > 0:
    if p == 1:
        num = float(input('Informe os números: '))
        soma1 = i+num
        p += 1
        f += 1
    else:
        num = float(input('Informe os números: '))
        soma1 += num
        f += 1


print('A média dos números digitados é: {}'.format(soma1/f))