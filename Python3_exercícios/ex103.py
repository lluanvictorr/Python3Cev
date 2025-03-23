def ficha(jogador='Desconhecido', gol=0):
    print(f'Jogador {jogador} fez {gol} gols no campeonato!')





nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
