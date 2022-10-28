salário = float(input('Digite o valor do seu salário: '))
if salário > 1250:
    print('Quem ganhava {:.2f}, passa a ganhar {:.2f}.'.format(
        salário, salário + (salário * 10)/100))
else:
    print('Quem ganhava {:.2f}, passa a ganhar {:.2f}.'.format(
        salário, salário + (salário * 15/100)))
