# faz a solicitação de número inteiro dentro do while
# verifica se é maior que zero (se for, imprime na tela o que ele é e peda mais números)
# identifica se é zero ou maior que zero e faz a mesma coisa do passo anterior
# garantir que o usuário digitará 10 números

i = 0

while i < 10:
    num = float(input('Digite um número inteiro: '))
    numt = int(num // 1)
    if numt < 0:
        print('Número é menor que zero')
    elif numt == 0:
        print('Número é zero')
    elif numt > 0:
        print('Número é positivo')
    i += 1