# Fzr um while infinito e colocar os inputs dentro dele
# Usar uma soma pra colocar os valores pedidos
# usar um if com um break pra finalizar o processo e mostrar a soma

i = 0
j = 2
soma = 0

while i < j:
    num = int(input('Digite um número inteiro: '))
    teste = num % 2
    if num < 0:
        print(soma)
        break
    elif teste != 0:
        print(soma)
        break
    soma += num