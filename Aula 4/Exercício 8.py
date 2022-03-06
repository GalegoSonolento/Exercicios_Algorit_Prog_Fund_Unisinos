# Exercício 8. Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:

# Digite 1 para somar dois valores
# Digite 2 para subtrair dois valores
# Digite 3 para multiplicar dois valores
# Digite 4 para dividir dois valores
# Digite 5 para realizar uma potência entre dois valores
# Digite 6 para realizar uma radiciação entre dois valores
# Digite qualquer outro número para sair
# De acordo com a opção informada pelo usuário, solicite os valores necessários para o usuário e imprima na tela o resultado da operação realizada.

print('Digite dois valores para o cálculo.')
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

print('Digite 1 para somar dois valores')
print('Digite 2 para subtrair dois valores')
print('Digite 3 para multiplicar dois valores')
print('Digite 4 para dividir dois valores')
print('Digite 5 para realizar uma potência entre dois valores')
print('Digite 6 para realizar uma radiciação entre dois valores')
print('Digite qualquer outro número para sair')
escolha = int(input('Agora, escolha a ação matemática: '))

if escolha == 1:
    print(num1+num2)
elif escolha == 2:
    print(num1-num2)
elif escolha == 3:
    print(num1*num2)
elif escolha == 4:
    print(num1/num2)
elif escolha == 5:
    print(num1**num2)
elif escolha == 6:
    print(num1**(1/num2))
else:
    print('Operação cancelada!')