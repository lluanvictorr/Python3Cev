from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
soma = n1 + n2
multiplicação = n1 * n2


while opção != 5:
    print('Escolha uma das funções a seguir:')
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        print('A soma de {} + {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        print('A multiplicação de {} X {} é {}.'.format(n1, n2, multiplicação))

    elif opção == 3:
        if n1 > n2:
           maior = n1
        else:
            maior = n2
        print(' Entre {} e {} o maior número é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número:'))
    elif opção == 5:
        print('Saindo do programa.....')
        sleep(1)

    else:
        print('Opção inválida, tente novamente!')
    print('--------------------------------------')
    sleep(1)
print('Obrigado! Volte mais tarde.!')

