import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
num = int(input('Em que número eu pensei?: '))
lista = [0, 1, 2, 3, 4, 5]
sort = random.choice(lista)
print('PROCESSANDO...')
sleep(2)
print('Eu pensei no número {}.'.format(sort))
if sort == num:
    print('Nossa você tem muita sorte.')
    print('Parabéns você acertou!')
else:
    print('Que pena, você errou. Tente novamente!')
