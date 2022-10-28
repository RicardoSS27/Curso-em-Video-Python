import math
a = float(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O ângulo {}.\n Possue Seno {:.2f}.\n Possue Cosseno {:.2f}.\n Possue Tangente {:.2f}.'.format(a, sen, cos, tan))
