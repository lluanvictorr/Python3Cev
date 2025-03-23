time = []
jogadores = dict()
quantidadeporpartida = []
while True:
    jogadores.clear()
    jogadores['Nome'] = str(input('Nome do jogador: '))
    totalpartidas = int(input(f'Quantidade de partidas que {jogadores["Nome"]} jogou: ' ))
    quantidadeporpartida.clear()
    for c in range(0, totalpartidas):
     quantidadeporpartida.append(int(input(f'Quantidade de gols na {c+1}º partida: ')))
    jogadores['Qnt de gols'] = quantidadeporpartida[:]
    jogadores['Gols TOTAL'] = sum(quantidadeporpartida)
    pergunta = str(input('Quer continuar?[S/N]')).upper()[0]
    time.append(jogadores.copy())
    while pergunta not in 'SN':
        print('Por favor digite apenas S ou N.')
        pergunta = str(input('Quer continuar?[S/N]')).upper()[0]
    if pergunta == 'N':
        break
print('=-'*25)
print(f' Cod ', end='')
for elemento in jogadores.keys():
    print(f'{elemento:<10} ', end='')
print()
for key, valor in enumerate(time):
    print(f'{key:>3}  ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('=-'*25)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 interrompe.)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com este código!')
    else:
        print(f'----- JOGADOR {time[busca]["Nome"]}: -----')
        for posição, gols in enumerate(time[busca]['Qnt de gols']):
            print(f'No {posição+1} jogo foram feitos {gols} gols.')
    print()
print('CERTO! ATÉ A PRÓXIMA!')
