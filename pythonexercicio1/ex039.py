from datetime import date
print('''Informe seu Genêro:
[ 1 ] MASCULINO
[ 2 ] FEMININO''')
gen = int(input('Sua opção: '))
nasc = int(input('Informe seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if gen == 2:
    print('Seu alistamento não é obrigatório.')
if gen == 1 and idade == 18:
    print('Está na hora de se alistar IMEDIATAMENTE!')
elif gen == 1 and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
elif gen == 1 and idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(atual + saldo))
