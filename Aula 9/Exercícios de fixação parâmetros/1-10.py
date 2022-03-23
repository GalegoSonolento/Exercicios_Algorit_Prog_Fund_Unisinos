# Exercício 1: Crie um método chamado imprimeValor, que recebe um valor qualquer por parâmetro e imprime-o na tela.
def imprimeValor(a):
    return a

# Exercício 2: Crie um método chamado somaValores que recebe dois valores por
# parâmetro e imprime na tela a soma dos dois valores.
def somaValores(a, b):
    return ('A soma é {}'.format(a + b))

# Exercício 3: Crie um método que recebe dois valores val1 e val2
# (assuma que serão inteiros).
# O método deve retornar verdadeiro se val1
# for divisível por val2 e falso caso contrário.
def maior(a, b):
    val1 = a
    val2 = b
    return a % b == 0

# Exercício 4: Crie um método chamado maiorValor que recebe 3 valores
# por parâmetro (assuma que serão inteiros) e retorna o maior dos três valores.
def maiorValor(a, b, c):
    valores = [a, b, c]
    base = 0
    cont = 0
    for i in valores:
        if cont == 0:
            base = i
            cont += 1
        elif base > i:
            base = i
            cont += 1
    return base

# Exercício 5: Crie um método que recebe um valor por parâmetro
# (assuma que será inteiro) e retorna a soma de todos os valores entre 0 e
# o valor recebido. Caso o valor seja negativo, o método deve retornar -1.
def soma(a):
    somar = 0
    if a < 0:
        return -1
    else:
        for n in range(0, a+1):
            somar += n
    return somar

# Exercício 6: Crie um método que recebe um valor por parâmetro
# (assuma que será uma string) e retorna a quantidade de letras
# que existem neste texto.
def numLetras(a):
    tam = len(a)
    return tam

# Exercício 7: Crie um método que recebe uma lista por parâmetro
# e imprime os elementos da lista recebida.
def lista(a):
    return a

# Exercício 8: Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string)
# e retorna a menor string da lista (com menos caracteres).
def listaString(a):
    base = 0
    cont = 0
    for i in a:
        if cont == 0:
            base = i
            cont += 1
        elif len(i) < len(base):
            base = i
            cont += 1
    return base

# Exercício 9: Crie um método que recebe dois parâmetros,
# que serão um inteiro N e uma string S (nesta ordem).
# O método deve imprimir na tela N vezes a string S.
def repetir(N, S):
    return (S*N)

teste = ['otorrinolaringologista', 'batata assada', 'anacleto']

# Exercício 10: Depois dos métodos criados, chame todos os métodos acima,
# passando os parâmetros correspondentes e SEMPRE SOLICITANDO OS PARÂMETROS
# PELO TECLADO, imprimindo na tela o retorno (para os que retornam algum valor).
met1 = imprimeValor(float(input('Digite um número: ')))
n1 = float(input('Escreva outro valor: '))
n2 = float(input('EScreva outro valor: '))
met2 = somaValores(n1, n2)
met3 = maior(n1, n2)
n3 = float(input('Digite mais um valor: '))
met4 = maiorValor(n1, n2, n3)
n4 = int(input('Digite um valor inteiro: '))
met5 = soma(n4)
str1 = input('Escreva uma pequena frase: ')
met6 = numLetras(str1)
print('Escreva itens de uma lista de compras: ')
listaCompras = []
i1 = input('Item 1: ')
i2 = input('Item 2: ')
i3 = input('Item 3: ')
listaCompras.append(i1)
listaCompras.append(i2)
listaCompras.append(i3)
met7 = lista(listaCompras)
met8 = listaString(listaCompras)
vezes = int(input('Escreva quantas vezes a pequena frase será repetida: '))
met9 = repetir(vezes, str1)

print(met1)
print(met2)
print(met3)
print(met4)
print(met5)
print(met6)
print(met7)
print(met8)
print(met9)
