n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
média = (n1 + n2) / 2
print('A média da pessoa que tirou {:.1f} e {:.1f}. É {:.1f}.'.format(
    n1, n2, média))
if média > 7:
    print('Sua média foi boa e você está APROVADO.')
elif 6.9 > média > 5:
    print('Sua média não foi tão boa e você está de RECUPERAÇÃO.')
elif média < 5:
    print('Sua média foi ruim e você está REPROVADO.')
