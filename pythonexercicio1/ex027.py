nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.count(' ')
n = nome.split()


print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[n1]))
# print('Seu último nome é {}.'.format(n[len(nome)-1)]))
