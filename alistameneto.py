import datetime
nas = int(input('coloque o seu ano de nascimento'))
atual = datetime.date.today().year
idade = atual - nas
if idade < 18:
    print('ta liberado')
elif idade == 18:
    print('ta na hora irmão')
elif idade > 18:
    print('ja passou da hora')
