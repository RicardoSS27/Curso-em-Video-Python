'''cid = str(input('Digite o nome da sua cidade:')).strip()
print('Analisando se a sua cidade começa com "Santo"')
print(cid.find('santo'))'''
cid = str(input('Que cidade você nasceu? ')).strip()
print('Analisando se a sua cidade começa com "Santo"')
print(cid[:5].upper() == 'SANTO')
