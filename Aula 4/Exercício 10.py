# Exercício 10. Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal
# ou uma consoante.

print('Digite uma letra para identificação de vogal ou consoante.')

letra = input('Digite sua letra para análise: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Sua letra é uma vogal!')
else:
    print('Sua letra é uma consoante!')