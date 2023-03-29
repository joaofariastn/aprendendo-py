vc = float(input('valor da casa'))
sl = float(input('valor do salario'))
anos = int(input('quantos anos vc quer pagar'))
pc = vc / (anos * 12)
if sl * 0.30 > pc:
    print(f' \033[1;30;46mfinanciamento foi aprovado a parcela ficara no valor de {pc}')
else:
    print('\033[1;31;40m seu financiamento foi negado nunca mais volte seu pobre')