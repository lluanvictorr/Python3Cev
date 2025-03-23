pessoas = []
dados = []
listapesada = list()
listaleve = list()
maiorpeso = 0
menorpeso = 0
while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(float(input('Informe o peso: ')))
    if len(pessoas) == 0:
      maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    pergunta = ' '
    pergunta = str(input('Quer continuar? [S/N]'.upper()))
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]'.upper()))
    if pergunta == 'N':
        break
print('=-' * 25)
print(f'Total de {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi de {maiorpeso} Kg',end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'E o menor peso foi de {menorpeso} Kg', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')