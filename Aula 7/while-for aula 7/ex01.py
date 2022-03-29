for i in range(0, 10):
    num = float(input('Digite um número aleatório: '))
    if num < 0:
        print('Número negativo')
    elif num == 0:
        print('Número é zero')
    elif num > 0:
        print('Número positivo')
