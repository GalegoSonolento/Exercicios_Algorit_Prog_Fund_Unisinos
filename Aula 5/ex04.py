import time
print('Digite \"IC" para iniciar uma contagem decrescente')

i = 1000
num = 1000

start = input('Começar?: ')

while num > 0:
    print(num)
    i -= 1
    num -= 1

print('Contagem regressiva finalizada')