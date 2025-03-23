números = (int(input('Digite um número: ')),
          int(input('Digite outro: ')),
          int(input('Digite mais um: ')),
          int(input('Agora o último: ')))
print(f'Você digitou os valores : {números}')
print(f'O número 9 apareceu {números.count(9)} vezes.')
if 3 in números:
    print(f'O número 3 apareceu na {números.index(3)}ª posição.')
else:
    print(F'O valor 3 não foi digitado em nenhuma posição!')
print('Os números pares digitados foram:', end=' ')
for n in números:
    if n % 2 == 0:
        print(n, end=' ')

print('\nPROGRAMA FINALIZADO...')


















