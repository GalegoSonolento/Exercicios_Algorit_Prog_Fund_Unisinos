# Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso seja um valor primo e
# falso caso contrário. Caso o parâmetro seja negativo o método deve retornar falso.

def numPrimo(a):
    if a < 0:
        return 'Falso'
    elif a == 1 or a == 0:
        return 'Falso'
    isPrimo = True
    cont = 2
    while cont < a:
        if a % cont == 0:
            isPrimo = False
        cont += 1
    if isPrimo:
        return 'Verdadeiro'
    else:
        return 'Falso'

num = int(input('Digite um valor inteiro: '))
print(numPrimo(num))
