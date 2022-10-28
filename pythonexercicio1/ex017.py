import math
'''b = float(input('Digite um valor para o cateto oposto:'))
c = float(input('Digite outro valor para o cateto adjacente:'))
x = (b**2) + (c**2)
a = math.sqrt(x)
print(' A hipotenusa desse triângulo retângulo é {:.2f} .'.format(a))'''

co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}.'.format(hi))
