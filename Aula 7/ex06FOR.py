# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado.
# Ao final, imprima apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

listaSolteiras = []
listaCasadas = []
listaDivorciadas = []
listaViuvas = []

print('Digite nomes e estados civis de 20 pessoas')

for i in range (0, 3):
    nome = input('Digite o nome: ')
    estadoCivil = input("Digite o estado civil: ")
    estadoCivil = estadoCivil.lower()
    if estadoCivil == 'solteira':
        listaSolteiras.append(nome)
    elif estadoCivil == 'casada':
        listaCasadas.append(nome)
    elif estadoCivil == 'divorciada':
        listaDivorciadas.append(nome)
    elif estadoCivil == 'viuva':
        listaViuvas.append(nome)
    else:
        print('Estado civil inválido')

print('Pessoas solteiras: ')
for p in listaSolteiras:
    print(p)
print('Pessoas casadas: ')
for p in listaCasadas:
    print(p)
print('Pessoas divorciadas: ')
for p in listaDivorciadas:
    print(p)
print('Pessoas viúvas: ')
for p in listaViuvas:
    print(p)