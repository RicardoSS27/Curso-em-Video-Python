'''nome = str(input('Digite seu nome completo:')).strip()
frased = nome.split()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
a = int(len(frased))
b = int(len(nome))
c = b - a + 1
print('Seu nome completo possui {} letras.'.format(c))
#frased = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(frased[0], len(frased[0])))'''


'''print('A frase apartir do 5° caractere de 2 em 2 é {}.'.format(frase[5::2]))
print('A frase possui {} caracteres E.'.format(frase.count('e')))
print('A parte dev começa na posição {}.'.format(frase.find('dev')))
print('A frase possui os caracteres dev?', '\n', 'dev' in frase)'''

nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome completo possui {} letras.'.format(len(nome) - nome.count(' ')))
nomed = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(
    nomed[0], len(nomed[0])))
