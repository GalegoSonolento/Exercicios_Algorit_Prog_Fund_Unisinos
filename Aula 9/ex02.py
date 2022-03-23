# Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido pela média aritmética das notas.
# Os conceitos são:
#
# - entre 0.0 e 4.0 (inclusive): conceito "D"
# - entre 4.0 (não incluído) e 7.0 (inclusive): conceito "C"
# - entre 7.0 (não incluído) e 9.0 (inclusive): conceito "B"
# - entre 9.0 (não incluído) e 10.0 (inclusive): conceito "A"
#
# Caso alguma das notas digitadas seja negativa, retorne o texto "ERRO"

def parametros(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 'ERRO'
    elif a > 10 or b > 10 or c > 10:
        return 'ERRO'
    media = (a + b + c)/3
    if 0.0 == media <= 4.0:
        return 'Conceito \'D\''
    elif 4.0 < media <= 7.0:
        return 'Conceito \'C\''
    elif 7.0 < media <= 9.0:
        return 'Conceito \'B\''
    elif 9.0 < media <= 10.0:
        return 'Conceito \'A\''

print('Digite suas notas para o cálculo da média')
d = float(input('Digite a primeira nota: '))
e = float(input('Digite a segunda nota: '))
f = float(input('Digite a terceira nota: '))

conceito = parametros(d, e, f)

print(conceito)