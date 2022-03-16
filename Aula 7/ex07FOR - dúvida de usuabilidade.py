# Crie um programa que solicita ao usuário que ele defina sua senha. A senha deve ser um texto (string) composto
# apenas por dígitos e deve ter entre 5 e 10 valores. O usuário tem apenas 6 chances de definir corretamente a senha.
# Caso ele defina corretamente a senha nas tentativas que ele tem, imprima uma mensagem de sucesso. Caso ele não
# defina a senha corretamente, imprima uma mensagem de insucesso. Dica: na aula aprendemos a ver se uma string é
# formada apenas por dígitos e aprendemos a descobrir o tamanho do texto digitado.
#
# O que eu preciso fazer:
# - identificar o tamanho da senha 5<=senha>=10
# - Identificar se ela contém números - Se as duas afirmações foram
#   falsas dá pra confirmar a senha
# - Esse processo tem que ser feito dentro de um while ou for pra conter o número de
#   chances que a pessoa tem pra colocar uma senha

numerais = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
acerto = True

for j in range (0, 6):
    senha = input('Defina sua senha, ela pode conter apenas de 5 a 10 letras: ')
    i = 0
    n = 0
    for x in senha:
        for p in numerais:
            if x == p:
                n += 1
        i += 1
    if i < 5:
        print('Senha inválida')
    elif i > 10:
        print('Senha inválida 2')
    elif n >= 1:
        print('Senha com números ')
    else:
        print('Senha aceita')
        acerto = False
        break

if acerto:
    print('Quantidade de tentativas excedida')

# errou = True
#
# for i in range (0, 6):
#     senha = input('Digite a senha')
#     if senha.isalpha() and 5 <= len(senha) <= 10:
#         print('Senha aceita')
#         errou = False
#         break
#     else:
#         print('Senha inválida')
#
# if errou:
#     print('Número de tentativas acabou')