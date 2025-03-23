soma = 0
contador = 0
for par in range(1, 7):
    numero = int(input('Digite o {}º: '.format(par)))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador +1
print('Você digitou {} números pares, e a soma deles é {} '.format(contador, soma))

