nome = str(input('coloque seu nome')).strip().upper()
print('o nome aparece {} A'.format(nome.count('A')))
print('a letra A aparece a primeira vez na posiçao {}'.format(nome.find('A')+1))
print('a ultima letra A aparece na {} posição'.format(nome.rfind('A')+1))
