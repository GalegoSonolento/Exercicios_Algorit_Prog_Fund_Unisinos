while True:
    num = int(input('Digite um número inteiro: '))
    lista = []
    div = 0
    soma = 0
    if num < 0:
        break

    while True:
        div += 1
        if num % div == 0:
            lista.append(div)
        if div == num-1:
            break

    for i in range(len(lista)):
        soma += lista[i]

    if soma == num:
        print('O número digitado é perfeito')
    else:
        print('O número digitado não é perfeito')
