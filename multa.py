vl = float(input('coloque o kilometro'))
if vl > 80:
    m = (vl - 80) * 7
    print('sua multa foi {}'.format(m))
else:
    print('boa viagem')