i = 0

while i < 3:
    user = input('Usuário: ')
    senha = input('Senha: ')

    if user == 'USER10' and senha == 'PASSWORD1234':
        print('LOGIN EFETUADO COM SUCESSO')
        break
    i += 1

    print('Usuário ou senha incorreto/os. Digite novamente')

print('Número de tentativas excedido')