matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], []]
somapar = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]:  '))
    if linha and coluna % 2 == 0:
        matriz[3].append(linha)
        matriz[3].append(coluna)
        soma = matriz[3]
print('=-' * 25)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print('=-'*25)
print(f'A soma so valores pares é: {somapar}')
for linha in range(0,3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {somacoluna}')
for c in range(0,3):
    if c == 0:
        maior = matriz[linha][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')