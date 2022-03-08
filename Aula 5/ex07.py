print('Digite 10 valores a serem somados no espaço abaixo.')

i = 0
soma = 0

while i < 10:
    num = int(input('Digite um número inteiro: '))
    i += 1
    soma += num

print('Sua soma é: {}'.format(soma))