# Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente,
# solicite que ele informe quantos produtos serão adicionados na lista.
# Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e armazene em uma lista.
# Ao final, imprima a lista de compras do usuário.


listaDCompras = []

num = int(input('Informe quantos itens sua lista terá: '))

for i in range (0, num):
    listaDCompras.append(input('Adicione um item'))

# print('Sua lista de compras contém: {}'.format(listaDCompras)) -> em algum caso isso é certo?
print('Lista de compras: ')
for i in listaDCompras:
    print(i)