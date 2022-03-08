print('Digite \"iniciar" e o programa contará até 1000')

inicio = input('(Iniciar): ')
i = 0
num = 0

if inicio == 'iniciar':
    while i<1000:
       print(num+1)
       num += 1
       i += 1

print('Contagem finalizada')