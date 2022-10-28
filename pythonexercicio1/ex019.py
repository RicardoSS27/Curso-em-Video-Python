import random
print('Vamos sortear 1 aluno para a vaga.')
n1 = str(input('Digite o nome do aluno:'))
n2 = str(input('Digite o nome do outro aluno:'))
n3 = str(input('Digite o nome do outro aluno:'))
n4 = str(input('Digite o nome do outro aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
