print('Digite 20 números com ponto flutuante no espaço indicado ')

i = 0

resultado = 'Os números digitados foram: '

while i < 20:
    valor = float(input('Digite o valor decimal:'))
    i += 1
    resultado += str(valor)
    resultado += ', '

print(resultado)
