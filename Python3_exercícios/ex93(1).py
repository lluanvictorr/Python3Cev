jogador = dict()
quantidadeporpartida = []
jogador['Nome'] = str(input('Nome do jogador: '))
totalpartidas = int(input('Quantidade de partidas jogadas: '))
for c in range(0, totalpartidas):
    quantidadeporpartida.append(int(input(f'Quantidade de gols na {c+1}º partida: ')))
jogador['Qnt de gols'] = quantidadeporpartida.copy()
jogador['Total de gols'] = sum(quantidadeporpartida)
print('--'*30)
for key, valor in jogador.items():
    print(f'{key} ---> {valor}')
print('--'*30)
print(f'O jogador {jogador["Nome"]} jogou ao todo {len(quantidadeporpartida)} partidas')
for posição, valor in enumerate(jogador["Qnt de gols"]):
    print(f'{posição+1}º partida total de {valor} gols')
print(f'E o total de gols do jogador {jogador["Nome"]} foi {jogador["Total de gols"]}')