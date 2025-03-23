número = contador = soma = 0
número = int(input('Digite um número [Digite 999 para parar]: '))
while número != 999:
    soma += número
    contador += 1
    número = int(input('Digite um número [Digite 999 para parar]: '))
print('Você digitou {} números, e a soma entre eles foi {}.'.format(contador, soma))

print('Terminou!')