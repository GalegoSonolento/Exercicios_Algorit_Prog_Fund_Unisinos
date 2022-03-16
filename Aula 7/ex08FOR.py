# Crie um programa que separa o joie do trigo. Seu programa deve ler a lista abaixo e criar duas listas diferentes:
# uma com todas as ocorrências da palavra "joio" e outra com todas as ocorrências da palavra "trigo". Ao final,
# imprima as listas separadas. Copie e cole a linha abaixo no seu código e complete o programa:

# Passos:
# - Copiar a lista
# - Criar um programa for para ler a lista
# - Criar um for dentro do for para identificação ou if e elif para identificar a palavra e colocar na lista certa
# - Usar 2 prints ao final para mostras as listas (ainda não sei como dispô-las, talvez ficasse melhor em lista mesmo)

joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio",
              "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
              "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio",
              "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio",
              "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
              "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio",
              "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
              "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio",
              "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio",
              "trigo", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio"]

joio = []
trigo = []
j = 0
t = 0

for x in joioETrigo:
    if x == 'joio':
        joio.append(x)
        j += 1
    elif x == 'trigo':
        trigo.append(x)
        t += 1

# for i in joio:
#     print(i)
# for p in trigo:
#     print(p)

print('Joios: {}'.format(joio))
print('-'*12)
print('Trigos: {}'.format(trigo))
print('Ao total, existem {} joios e {} trigos.'.format(j, t))