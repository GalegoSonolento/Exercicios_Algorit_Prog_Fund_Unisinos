print('Digite quantos números serão digitados no espaço e digite-os logo após')

quant = int(input('Quantos números serão digitados? '))
i = 1
nums = 'Os números digitados foram: '

while i <= quant:
    num = int(input('Digite um dos números: '))
    if num == 0:
        print('O número é zero')
    elif num > 0:
        print('O número é positivo')
    elif num < 0:
        print('O número é negativo')
    if i == quant:
        nums += str(num) + '.'
    else:
        nums += str(num) + ', '
    i += 1

print(nums)

