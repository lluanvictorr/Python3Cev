sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe seu sexo (M/F): ')).strip().upper()[0]
print('Sexo {} informado, obrigado!'.format(sexo))

