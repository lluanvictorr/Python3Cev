jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input(f'Quantidade de partidas que {jogador["Nome"]} jogou: '))
for c in range(0, totalpartidas):
    partidas.append(int(input(f'Quantidade de gols na {c + 1}ª partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total de gols'] = sum(partidas)
print('=-'*25)
for key, valor in jogador.items():
    print(f'{key}: {valor}')
print('=-'*25)
print(f'O jogador {jogador["Nome"]} jogou ao total {len(jogador["Gols"])} partidas.')
for posição, valor in enumerate(jogador['Gols']):
    print(f'{posição + 1}ª partida foram {valor} gols.')
print(f'Total de {jogador["Total de gols"]} gols de {jogador["Nome"]}.')

