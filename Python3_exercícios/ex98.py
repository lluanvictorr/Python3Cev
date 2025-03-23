from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    sleep(1.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
       contagem = i
       while contagem <= f:
        print(f'{contagem}', end='  ')
        sleep(0.5)
        contagem += p
       print(f'ACABOU!')
    else:
        contagem = i
        while contagem >= f:
            print(f'{contagem}', end=' ')
            sleep(0.5)
            contagem -= p
        print('ACABOU!')
    print('-=' * 30)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de decidir como vai ser a contagem!')
inicio = int(input('Inicio da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('De quanto em quanto: '))
print("=-" * 30)
contador(inicio, fim, passo)
