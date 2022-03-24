def somaPositivos(a, b):
    if a > 0 and b > 0:
        return a+b
    else:
        return -1

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print('Erro, não é possível realizar uma divisão por zero')
        return 0

def verificaTriangulo(x, y, z):
    if abs(y - z) < x < (y + z) or abs(x - z) < y < (x + z) or abs(x - y) < z < (x + y):
        if x == y == z:
            return 'Seu triângulo é esquilátero'
        elif x != y and x != z and y != z:
            return 'Seu triângulo é escaleno'
        else:
            return 'Seu triângulo é isóceles'
    else:
        return 'Seus valores não criam um triângulo'

def verificaIdade(a):
    if a < 0:
        return 'Erro, menor que zero'
    elif 0 <= a <= 12:
        return 'Criança'
    elif 13 <= a <= 18:
        return 'Adolescente'
    elif 19 <= a <= 120:
        return 'Adulto'
    elif a > 120:
        return 'Erro, maior que 102'

def sinaleira(a):
    a = a.lower()
    if a == 'verde':
        print('Aberta')
    elif a == 'vermelho':
        print('Fechada')
    elif a == 'amarelo':
        print('Atenção')
    else:
        print('Erro')

def contador(x):
    for i in range(x, 301):
        print(i)

def verificaPrimo(a):
    isPrimo = True
    quant = 2
    while quant < a:
        if a % quant == 0:
            isPrimo = False
        quant += 1
    return isPrimo

def achaMaior(x, y, z):
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    elif z > x and z > y:
        print(z)

def imprimePares(x):
    for p in range(0, x):
        if p % 2 == 0:
            print(p)


while True:
    print('Dentre as seguintes opções: \n 1. Soma positivos \n 2. Divide'
          '\n 3. Verifica triângulo \n 4. Verifica idade \n '
          '5. Sinaleira \n 6. Conta até 300 \n 7. Verifica Primo \n 8. Acha maior'
          '\n 9. Imrime pares')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print(somaPositivos(int(input('Digite um valor: ')), int(input('Digite outro: '))))
        print(input('Digite algo para continuar: '))
    elif opcao == 2:
        print(divide(int(input('Digite um valor: ')), int(input('Digite outro: '))))
        print(input('Digite algo para continuar: '))
    elif opcao == 3:
        print(verificaTriangulo(int(input('Digite um valor para o triângulo: ')), int(input('Digite outro: ')),
                                int(input('Digite outro: '))))
        print(input('Digite algo para continuar: '))
    elif opcao == 4:
        print(verificaIdade(int(input('Digite sua idade: '))))
        print(input('Digite algo para continuar: '))
    elif opcao == 5:
        sinaleira(input('Digite uma das coras de sinaleira: '))
        print(input('Digite algo para continuar: '))
    elif opcao == 6:
        contador(int(input('Digite um valor inteiro para o contador: ')))
        print(input('Digite algo para continuar: '))
    elif opcao == 7:
        print(verificaPrimo(int(input('Digite um valor para verificar se é primo: '))))
        print(input('Digite algo para continuar: '))
    elif opcao == 8:
        achaMaior(int(input('Digite um valor: ')), int(input('Digite outro: ')), int(input('Digite outro: ')))
        print(input('Digite algo para continuar: '))
    elif opcao == 9:
        imprimePares(int(input('Digite um valor para expressar os pares até ele: ')))
        print(input('Digite algo para continuar: '))
    else:
        print('Você digitou uma opção inválida')
        break
