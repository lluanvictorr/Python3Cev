maiorpeso = 0
menorpeso = 0

for pessoas in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '. format(pessoas)))
    if pessoas == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {} Kg'.format(maiorpeso))
print('O menor peso lido foi de {}Kg'.format(menorpeso))

