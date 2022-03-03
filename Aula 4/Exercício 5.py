print('Crie um programa que recebe o preço de um produto pelo teclado e imprime na tela a mensagem adequada, de acordo com o preço: ')
print("“Preço inválido”, se o preço for negativo ou zero")
print("“Preço baixo”, se o preço for entre 0 e 30 (inclusive)")
print('“Preço médio”, se o preço for entre 30 e 50 (inclusive)')
print('“Preço alto”, se o preço for maior do que 50')


print('Coloque o preço de seu produto que exibiremos ')
preco = int(input('Coloque o preço do produto: '))

if preco <= 0:
    print('Preço inválido!')
elif 0 < preco <= 30:
    print('Preço baixo!')
elif 30 < preco <= 50:
    print('Preço médio!')
else:
    print('Preço alto!')