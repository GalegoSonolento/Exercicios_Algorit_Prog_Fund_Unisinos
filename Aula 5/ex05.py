print('O programa avai perguntar o time do usuário. No final ele vai dizer o número de pessoas que torcem para o '
      'Grêmio, dentre as 10 questionadas.')

i = 0
gremista = 0

while i <13:
    time = input('Digite o nome de seu time: ')
    if time == 'Grêmio':
        gremista += 1
    i += 1

print('Existem {} gremistas no grupo.'.format(gremista))