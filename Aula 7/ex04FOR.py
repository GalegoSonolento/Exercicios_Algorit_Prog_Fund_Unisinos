texto = input('Digite um pequeno texto: ')
vogais = ['a', 'e', 'i', 'o', 'u']
soma = 0

for x in texto:
    for i in vogais:
        if x == i:
            soma += 1

print(soma)