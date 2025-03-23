valores = []
quantidade = 0
pergunta = ' '
while True:
    valores.append(int(input('Digite um valor: ')))
    pergunta = str(input('Quer digitar mais um valor? [S/N]: ').upper())
    while pergunta not in 'SN':
      pergunta = str(input('Quer digitar mais um valor? [S/N]: ').upper())
    if pergunta == 'N':
        break
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valores}')
if 5 in valores:
    print('O número 5 foi registrado!')
else:
    print('O número 5 não foi encontrado!')
