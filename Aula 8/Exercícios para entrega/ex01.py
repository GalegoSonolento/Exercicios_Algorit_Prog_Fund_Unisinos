# Criar um while infinito pra colocar as opções de uso
# input perguntando quantos meses quer analisar
# Criar uma lista para colocar os valores dos meses dentro
# Printar todos os valores dos meses
# Identificar se baixam ou não
# Perguntar se deseja continuar a análise ou sair dela

valMeses = []
media = 0
quant = 0

while True:
    quant = 0
    numMeses = int(input('Quantos meses quer analisar? '))
    for x in range (0, numMeses):
        valor = float(input('Digite a quantidade de audiência desse mês: '))
        valMeses.append(valor)
        if x == 0:
            primeiro = valor
            quant += 1
        else:
            if valor > primeiro:
                primeiro = valor
                quant += 1

    if numMeses == quant:
        msg = 'Sempre crescente'
    else:
        msg = 'Nem sempre crescente'
    for p in valMeses:
        media += p
    print('{}. Média da audiência: {}'.format(msg, (media/2)))
    pergunta = input('Deseja analisar outros meses(S/N)? ')
    if pergunta == 'S':
        print('-'*12)
    elif pergunta == 'N':
        break