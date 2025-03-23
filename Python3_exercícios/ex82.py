valores = []
valoresimpar = []
valorespar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    pergunta = ' '
    pergunta = str(input('Quer inserir mais um valor? [S/N] ').upper())
    while pergunta not in 'SN':
        pergunta = str(input('Quer inserir mais um valor? [S/N] ').upper())
    if pergunta == 'N':
            break
for posição, valor in enumerate(valores):
    if valor % 2 == 0:
        valorespar.append(valor)
    else:
        valoresimpar.append(valor)

print(f'Os valores informados foram: {valores}')
print(f'Os valores impares foram: {valoresimpar}')
print(f'E os valores pares foram: {valorespar}')
print('-='*25)
print('Obrigado!')

