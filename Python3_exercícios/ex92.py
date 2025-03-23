from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input('Digite o nome: '))
anonascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - anonascimento
pessoa['CTPS'] = int(input('Carteira de trabalho (0 se não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['idade'] + ((pessoa['anocontratação'] + 35) - datetime.now().year)
print('-='*25)
for key, valor in pessoa.items():
    print(f'{key}: {valor}')


