patos = int(input('Quantos patinhos você quer que passeiem? '))
i = 0
count = patos

while patos < 2:
    patos = int(input('O número de patinhos deve ser maior ou igual a 2: '))

i = 0
count = patos

while patos >= 2:
    print('{} patinhos \n Foram passear '
          '\n Além das montanhas \n Para brincar \n A mamãe gritou'
          '\n Quack quack quack'.format(patos))
    patos -= 1
    if patos == 1:
        print('Mas só {} patinhos \n Voltaram de lá'.format(patos))
    elif patos == 0:
        print('Mas nenhum patinho \n Voltou de lá.')
    else:
        print('Mas só {} patinhos \n Voltaram de lá.'.format(patos))
    print('-' * 12)
    i += 1
    patos -= 1

print('A mamãe patinha \n Foi procurar \n Além das montanhas \n Na beira do mar '
      '\n A mamãe gritou \n Quack quack quack \n E os {} patinhos \n Voltaram de lá'.format(count))

# print('2 patinhos foram passear \n Além das montanhas \n Para brincar '
#       '\n A mamãe gritou \n Quack quack quack \n Mas só 1 patinho '
#       '\n Voltou de lá')
#
# print('-'*12)

# print('1 patinho foi passear \n Além das montanhas \n Para brincar '
#       '\n A mamãe gritou \n Quack quack quack \n Mas nenhum patinho '
#       '\n Voltou de lá')
