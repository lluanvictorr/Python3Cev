from random import randint
computador = randint(0,10)
print('Sou o seu computador e acabei de pensar em número entre 0 e 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('É um número mais alto, tente outra vez!')
        elif jogador > computador:
            print('É um número mais baixo, tente denovo!')
print('Acertou o número! Com {} tentativas.'.format(palpites))
