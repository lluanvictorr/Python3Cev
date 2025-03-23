from time import sleep
from random import randint
from operator import itemgetter
print('-='*25)
print('                JOGANDO OS DADOS')
print('=-'*25)
sorteio = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4': randint(1,6)}
for k, v in sorteio.items():
    sleep(1.5)
    print(f' {k} tirou no dado: {v} ')
ranking = []
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('-='*25)
print('             RANKING DOS JOGADORES')
print('-='*25)
sleep(1)
for posição, valor in enumerate(ranking):
    print(f'{posição+1}º lugar {valor[0]} que tirou {valor[1]}')
    sleep(1)


