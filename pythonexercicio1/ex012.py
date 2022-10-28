produto = float(input('Qual preço do produto?'))
desconto = 5/100
p1 = produto * desconto
R = produto - p1
print(' o Valor do produto é R$:{}. Com o desconto de 5%, o valor é R$:{:.2f}.'.format(produto, R))
#print(' o Valor do produto é R$:{}. Com o desconto de 5%, o valor é R$:{:.2f}.'.format(produto, (produto - p1)))
