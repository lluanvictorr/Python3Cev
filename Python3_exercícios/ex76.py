print('='* 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 10.00,
         'Mochila', 120.50,
         'Caneta', 3.00,
         'Livros', 100.00)
for posição in range(0, len(lista)):
    if posição % 2 ==0:
        print(f'{lista[posição]:.<30}', end='')
    else:
        print(f'R${lista[posição]:>8.2f}')
print('='*40)