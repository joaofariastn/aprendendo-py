sl = float(input('qual é o seu salario'))
if sl <= 1250:
    sla = sl * 1.15
    print(f'\033[1;31;40mseu salario ficara {sla}\033')
else:
    sls = sl * 1.10
    print(f'\033[0;36;40mseu salario ficara {sls}\033[m')