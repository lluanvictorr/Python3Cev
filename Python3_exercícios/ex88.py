from time import sleep
from random import randint
print('=-'*25)
print('               SORTEIO MEGA SENA')
print('=-'*25)
lista = list()
jogos = list()
quantidade = int(input('Digite o quanto de jogos quer que seja sorteado: '))
total = 1

while total <= quantidade:
    contador = 0
    while True:
        número = randint(1, 60)
        if número not in lista:
         lista.append(número)
         contador += 1
        if contador >= 6:
         break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'SORTEANDO {quantidade} JOGOS...')
sleep(1)
for índice, lista in enumerate(jogos):
    sleep(1)
    print(f'Jogo {índice + 1}: {lista}')
    sleep(1)
print('=-'*25)
print('Se ganhar quero minha porcentagem deste prêmio!')


