pessoa = {}
totalpessoas = []
somaidade = 0
médiaidade = 0
totalmulher = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    somaidade += pessoa['Idade']
    totalpessoas.append(pessoa.copy())
    pergunta = ' '
    pergunta = str(input('Quer continuar? [S/N] ')).upper()[0]
    while pergunta not in 'SN':
        print('Apenas S ou N.')
        pergunta = str(input('Quer continuar?[S/N] ')).upper()[0]
    if pergunta == 'N':
        break
print(f'A) Total de pessoas cadastradas: {len(totalpessoas)}')
médiaidade = somaidade / len(totalpessoas)
print(f'B) A média de idade das pessoas cadastradas é de {médiaidade:5.2f} anos')
print('C) Mulheres cadastradas: ', end=' ')
for pessoa in totalpessoas:
    if pessoa['Sexo'] == 'F':
        print(f'{pessoa["Nome"]} /', end=' ')
print(f'\nD) Pessoas com a idade acima da média: ')
for pessoa in totalpessoas:
    if pessoa['Idade'] >= médiaidade:
     for key, valor in pessoa.items():
        print(f'{key} = {valor};',end=' ')
print()
print('-'*30)
print('Amostragem de dados ENCERRADA!')
print('-'*30)


