# Exercício 9. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será
# necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos). Caso algum valor informado seja
# negativo, informe uma mensagem de erro e não realize o cálculo.

print('Utilize essa calculadora para identificar a necessidade de Grau C.')

graua = float(input('Coloque a nota do grau A: '))
if graua < 0:
    print('Nota inválida. Digite novamente.')
    graua = float(input('Coloque a nota do grau A: '))
graub = float(input('Coloque a nota do grau B: '))
if graub < 0:
    print('Nota inválida. Digite novamente.')
    graub = float(input('Coloque a nota do grau B: '))

media = (graua*0.33)+(graub*0.67)

if media < 6:
    print('Sua nota e insuficiente. Necessitarás de Grau C.')
else:
    print('Parabéns! Você passou direto!')