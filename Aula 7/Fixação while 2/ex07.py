# while infinito
# Comparação de senha e usuário perfeitas

i = 0
j = 2

while i < j:
    user = input('Usuário: ')
    senha = input('Senha: ')

    if user == 'USER10' and senha == 'PASSWORD1234':
        print('LOGIN EFETUADO COM SUCESSO')
        break

    print('Usuário ou senha incorreto/os. Digite novamente')