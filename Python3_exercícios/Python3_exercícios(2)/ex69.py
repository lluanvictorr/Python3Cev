print('<>' * 15)
print(f'CADASTRO DE USUÁRIO')
print('<>' * 15)
maior = 0
totalmulher = 0
totalmulher20 = 0
quantidademaior = 0
quantidade = 0
totalhomem = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
            maior = idade
            quantidademaior += 1
    if idade < 20:
            menor = 0
            menor = idade

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? M/F: ')).upper()[0]
    if sexo == 'M':
        totalhomem += 1
    if sexo == 'F':
        totalmulher += 1
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resposta == 'N':
            break
print(f'{quantidademaior} pessoas tem mais de 18 anos, {totalhomem} homens foram cadastrados, {totalmulher} mulheres foram cadastradas e {totalmulher20} mulheres são menores de 20 anos')
