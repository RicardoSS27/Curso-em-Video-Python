peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em METROS? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}.'.format(imc))
if imc < 16:
    print('Seu peso classifica-se como: Magreza Grau III')
elif 16.0 >= imc <= 16.9:
    print('Seu peso classifica-se como: Magreza Grau II')
elif 17.0 >= imc <= 18.4:
    print('Seu peso classifica-se como: Magreza Grau I')
elif 18.5 >= imc <= 24.9:
    print('Seu peso classifica-se como: Adequado')
elif 25.0 >= imc <= 29.9:
    print('Seu peso classifica-se como: Pré-Obeso')
elif 30.0 >= imc <= 34.9:
    print('Seu peso classifica-se como: Obesidade Grau I')
elif 35.0 >= imc <= 39.9:
    print('Seu peso classifica-se como: Obesidade Grau II')
elif imc >= 40:
    print('Seu peso classifica-se como: Obesidade Mórbida')
