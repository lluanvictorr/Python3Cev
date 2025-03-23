números = []
pergunta = ' '
while True:
    número = int(input('Digite um número para ele ser cadastrado: '))
    if número not in números:
        números.append(número)
        print('Número cadastrado com sucesso!')
    else:
        print('Este número já está cadastrado! Se quiser digite outro...')
        pergunta = str(input('Quer cadastrar mais números? [S/N] '))
    pergunta = str(input('Quer cadastrar mais números? [S/N] '))
    while pergunta not in 'SsNn':
     pergunta = str(input('Quer cadastrar mais números? [S/N] '))
    if pergunta in 'Nn':
        break
números.sort()
print(f'Os números cadastrados foram {números}')

