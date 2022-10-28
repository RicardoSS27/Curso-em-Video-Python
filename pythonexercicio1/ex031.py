d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar a sua viagem de {:.2f}KM.'.format(d))
if d <= 200:
    print('O valor da sua passagem é R${:.2f}.'.format(d*0.5))
else:
    print('O valor da sua passagem é R${:.2f}.'.format(d*0.45))
print('Tenha uma boa viagem!')
