print('-=-'*20)
print('                  Analisador de Triângulos'.upper())
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end='')
    if r1 == r2 == r3:
        print('Forma um triângulo EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Forma um triângulo ISÓSCELES"')
    elif r1 != r2 != r3:
        print('Forma um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
