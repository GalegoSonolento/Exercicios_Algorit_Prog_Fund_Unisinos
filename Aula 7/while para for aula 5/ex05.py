# Crie um programa que solicita o time de 10 usuários pelo teclado.
# Ao final, imprima quantos torcedores torcem para o Grêmio

gremistas = 0

for n in range(0, 10):
    time = input('Para qual time você torce? ')
    time = time.lower()
    if time == 'gremio' or time == 'grêmio':
        gremistas += 1
print('No total foram encontrados {} gremistas'.format(gremistas))