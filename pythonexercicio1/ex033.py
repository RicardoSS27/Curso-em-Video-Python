a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior valor
maior = c
if b > c and b > a:
    maior = b
if a > c and a > b:
    maior = a
print('O menor valor digitado é {}.'.format(menor))
print('O maior valor digitado é {}.'.format(maior))
