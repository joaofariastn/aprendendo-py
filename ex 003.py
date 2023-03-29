nome_v = input("Digite o nome do vendedor: ")
salario_f = float(input("Digite o salário fixo do vendedor: "))
total_v = float(input("Digite o total de vendas efetuadas pelo vendedor (em dinheiro): "))
comissao = 0.15 * total_v
salario_fi = salario_f + comissao
print(f'Nome do vendedor: {nome_v}')
print(f'Salário fixo: R$ {salario_f}')
print(f'Salário final: R$ {salario_fi}')
if salario_fi >= 6000:
    print('otimo salario mano')
else:
    print('que merda de salario')

