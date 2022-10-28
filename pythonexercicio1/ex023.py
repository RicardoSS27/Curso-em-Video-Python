'''n = int(input('Digite um número de 0 a 9999:'))
m = n[0]
c = n[1]
d = n[2]
u = n[3]
print('O número {}.'.format(n))
print('Possui {} milhares.'.format(m), '\n', 'Possui {} Centenas.'.format(c))
print('Possui {} Dezenas.'.format(d), '\n', 'Possui {} Unidades.'.format(u))'''
n = int(input('Digite um número de 0 a 9999:'))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print('O número {}.'.format(n))
print('Possui {} milhares.'.format(m), '\n', 'Possui {} Centenas.'.format(c))
print('Possui {} Dezenas.'.format(d), '\n', 'Possui {} Unidades.'.format(u))
