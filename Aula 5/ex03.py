print('Dê o comando \"iniciar pares" e o programa contará os números pares até 2000')

i = 0
num = 0

comand = input('Começar: ')

while i<=2000:
    if num%2 == 0:
        print(num)
    i += 1
    num += 1

print('Contagem finalizada!')