from datetime import date
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Você é um atleta MIRIM!')
elif 10 >= idade < 14:
    print('Você é um atleta INFANTIL!')
elif 15 >= idade < 19:
    print('Você é um atleta JUNIOR!')
elif 20 >= idade < 25:
    print('Você é um atleta SÊNIOR!')
else:
    print('Você é um atleta MASTER!')
