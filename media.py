n = float(input('coloque sua nota'))
if n >= 7.0:
    print(f'sua nota foi {n} parabens vc foi \033[1;36;40mAPROVADO')
elif n <= 5.0:
    print(f'voce foi \033[1;31;40mREPROVADO')
else:
    print(f'Voce ta de \033[1;33;40mRECUPERACAO')