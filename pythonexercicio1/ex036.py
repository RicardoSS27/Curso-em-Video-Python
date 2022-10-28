casa = float(input('Qual o valor da sua casa? R$'))
salário = float(input('Qual o valor do salário do comprador mensalmente? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestmax = salário * 30 / 100
vpagar = casa / (anos * 12)
print('O valor da casa é {:.2f} financiada em {} anos.'.format(
    casa, anos), end='')
print('A prestação mensal será de {:.2f}.'.format(vpagar))
if vpagar <= prestmax:
    print('O seu score é positivo e a compra foi aprovada com sucesso.')
else:
    print('O seu score é insuficiente e sua compra foi negada.')
print('Agradeço pela atenção e tempo!')
