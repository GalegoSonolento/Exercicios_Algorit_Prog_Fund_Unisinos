# Pedir o nome de fulano
# Saudar e oferecer as opções
# Colocar um limitador para as 5 tentativas erradas
# Criar um path com cada uma das opções
# A opção sair tem que realmente sair do sistema

i = 0
j = 0
opcao = 0
nome = input('Digite seu nome: ')

while i < 2:
    if opcao == 'S':
      break
    print('Olá {}'.format(nome))
    print('Dentre as opções: \n 1) Verificar triângulo \n 2) Calcular equação do segundo grau \n 3) Conferir data \n '
          '4) Verificar tamanho do texto \n 5) Analisar CPF \n 6) Contar caracteres \n 7) Sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        while i < 2:
            j = 0
            print('Verifique se o triângulo é verdadeiro')
            a = int(input('Digite um valor para o triângulo: '))
            b = int(input('Digite outro: '))
            c = int(input('Digite outro: '))
            if abs(b-c) < a < (b+c) or abs(a-c)<b<(a+c) or abs(a-b)<c<(a+b):
                if a == b == c:
                    print('Seu triângulo é esquilátero')
                    break
                elif a != b and a != c and b != c:
                    print('Seu triângulo é escaleno')
                    break
                else:
                    print('Seu triângulo é isóceles')
                    break
            else:
                print('Seus valores não criam um triângulo')
                break
        opcao = input('Deseja voltar para o início ou sair(I/S)? ')
        if opcao == 'S':
            print('Obrigado por utilizar nosso sistema!')
            break
        elif opcao == 'I':
            print('Perfeito')
    elif opcao == 2:
        while True:
            j = 0
            print('Dê dados para calcular uma equação do 2° grau')
            a = float(input('Digite o valor de a: '))
            if a == 0.0:
                print('Você não está gerando uma equação do 2° grau')
                opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                a += 1
                break
            b = float(input('Digite o valor de b: '))
            c = float(input('Digite o valor de c: '))
            delta = ((b**2)-4*a*c)
            if delta < 0:
                print('A operação é impossível, já que o delta é negativo, impossibilitando a raiz quadrada')
            elif delta == 0:
                raiz = ((b*(-1)) + delta)
                print('Existe apenas uma raiz real')
                print('A raíz é: {}'.format(raiz))
            elif delta > 0:
                raiz1 = ((b*(-1))- delta)/(2*a)
                raiz2 = ((b*(-1)) + delta)/(2*a)
                print('Suas raízes são x\': {} e x\": {}'.format(raiz1, raiz2))
            opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                break
    elif opcao == 3:
        while True:
            meses = ['Janeiro', '1', 'Fevereiro', '2', 'Março', '3', 'Abril', '4', 'Maio', '5', 'Junho', '6', 'Julho', '7', 'Agosto', '8', 'Setembro', '9', 'Outubro', '10', 'Novembro', '11', 'Dezembro', '12']
            dia = int(input('Digite o dia da data: '))
            mes = input('Digite o mes da data: ')
            ano = int(input('Digite o ano: '))
            if 1 <= dia >= 31:
                print('Sua data é inválida')
            else:
                if mes == meses:
                    print('Sua data é válida')
                    print('Em teoria, os anos são todos válidos, mas eles podem ser colocados no futuro ou no passado')
                else:
                    print('Sua data é inválida')
            opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                break
    elif opcao == 4:
        while True:
            trecho = input('Digite um pequeno trecho de texto: ')
            x = len(trecho)
            if x < 5:
                print('O texto é muito pequeno.')
            elif 5 <= x < 15:
                print('Seu texto é de tamanho médio.')
            elif 15 <= x < 20:
                print('Seu texto é grande.')
            else:
                print('Seu texto é inválido.')
            opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                break
    elif opcao == 5:
        while True:
            cpf = input('Digite seu CPF: ')
            tam = len(cpf)
            teste = cpf.isdigit()
            if not teste:
                print('Você não digitou um CPF')
            elif teste:
                if 11 < tam:
                    print('Você não digitou um CPF')
                elif 11 > tam:
                    print('Você não digitou um CPF')
                elif tam == 11:
                    print('O CPF digitado é válido')
            opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                break
    elif opcao == 6:
        while True:
            quant = 0
            texto = input('Digite um pequeno texto: ')
            texto = texto.lower()
            tam = len(texto)
            testeVogais = ['a', 'e', 'i', 'o', 'u']
            for x in testeVogais:
                vogal = texto.count(x)
                quant += vogal
            espaco = texto.count(' ')
            outros = (tam - (quant + espaco))
            print('Seu texto possui {} vogais, {} espaços e {} caracteres variados.'.format(quant, espaco, outros))
            opcao = input('Deseja voltar para o início ou sair(I/S)?')
            if opcao == 'S':
                print('Obrigado por utilizar nosso sistema!')
                break
            elif opcao == 'I':
                break
    elif opcao == 7:
        j = 0
        print('Obrigado por utilizar nosso sistema!')
        break
    elif j == 5:
        print('Parece que você não está entendendo o funcionamento do sistema. Até mais.')
        break
    else:
        j += 1
        # Isso aqui é pra opção que for inválida
        print('Opção inválida')
        voltar = input('Digite algo para voltar à tela de menu: ')