from time import sleep
número = int(input('Digite um número para calcular seu fatorial: '))
contador = número
fatorial = 1
print('Calculando fatorial de {}.....'.format(número))
sleep(2)
print('{}! = '.format(número), end='')
while contador > 0:
    print(' {} '.format(contador),end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador -= 1
print(fatorial)


