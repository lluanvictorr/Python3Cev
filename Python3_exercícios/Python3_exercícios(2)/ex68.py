from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0,10)
    total = jogador + computador
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Você quer PAR ou ÍMPAR?[P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}, total de {total}.',end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
    if parouimpar == 'P':
        if total % 2 == 0:
            print('Jogador VENCEU!')
            vitoria += 1
        else:
            print('Computador VENCEU!')
            break
    elif parouimpar == 'I':
        if total % 2 == 1:
            print('Jogador VENCEU!')
            vitoria += 1
        else:
            print('Computador VENCEU!')
            break
    print('Vamos jogar novamente!')
print(f'FIM DE JOGO! Jogador obteve {vitoria} vitórias.')


