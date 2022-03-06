# Exercício 6. Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa
# aplicada deve ser:

# Aumento de 10% caso o valor seja menor do que 100
# Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
# Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
# Imprima uma mensagem de erro se o valor for negativo
# Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

print('Coloque os valores que calcularemos a taxa e juros e quanto deverá ser pago!')

valor = float(input('Insira o valor aqui: '))

if 0 < valor < 100:
    valor10 = valor * 0.1 + valor
    print('O pagamento deve ser:', valor10)
elif 100 <= valor < 300:
    valor20 = valor * 0.2 + valor
    print('O pagamento deve ser:', valor20)
elif 300 <= valor < 1000:
    valor50 = valor * 0.5 + valor
    print('O pagamento deve ser:', valor50)
elif valor <= 0:
    print('valor inválido, insira outro!')
else:
    print('Valores muito altos, os juros não foram definidos para quantias maiores que 1000!')
