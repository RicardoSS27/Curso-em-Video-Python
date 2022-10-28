v = float(input('Qual a velocidade atual do carro? '))
vmax = 80
multa = 7  # por km acima de 80km/h
if v <= vmax:
    print('Dirija com cuidado. BOA VIAGEM!')
else:
    print('Você está acima da velocidade permitida que é de 80km/h.')
    print('O valor que você deve pagar é {:.2f}.'.format((v-vmax) * multa))
