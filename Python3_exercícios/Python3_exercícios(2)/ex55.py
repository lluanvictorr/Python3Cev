from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = anoatual - nascimento
    if idade >= 21:
        totalmaior += 1
        print('Esta pessoa tem {} anos e já é considerada de maior'.format(idade))
    else:
        totalmenor += 1
        print('Esta pessoa tem {} anos, é considerada de menor'.format(idade))
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))

