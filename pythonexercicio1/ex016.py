'''num = float(input('Digite um número:'))
a = num // 1
b = num % 1
print('O número {}. Tem {:.0f} partes inteiras.'.format(num, num))
#print('O número escolhido foi {}. Esse número tem {} partes inteiras. E possui resto {:.3f}.'.format(num, a, b))'''

import math
#from math import trunc Para importar somente essa função da biblioteca, e usar apenas 'trunc'
num = float(input('Digite um número:'))
print('O número escolhido foi {}. E sua parte inteira é {}.'.format(num, math.trunc(num)))

'''num = float(input('Digite um número:'))
print('O número {}. Tem {} partes inteiras.'.format(num, int(num)))'''
