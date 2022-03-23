# Exercício 1: Crie um método que recebe um inteiro X por parâmetro e imprime os valores de 1 até X (inclusive).

def analiseNum(a):
    for i in range(1, a+1):
        print(i)

num = int(input('Digite um valor inteiro aqui: '))
analiseNum(num)