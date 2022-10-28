num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases da convesão:
[ 1 ] PARA BINÁRIO
[ 2 ] PARA OCTAL
[ 3 ] PARA HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}.'.format(num, bin(num)[2:]))
if opção == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num)[2:]))
if opção == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('Sua opção é inválida. Tente novamente.')
