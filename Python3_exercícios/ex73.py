tabela = ('Santos', 'Mirassol', 'Sport Recife', 'Ceará SC',
          'Novorizontino', 'Goiás', 'Operário', 'América-MG',
          'Vila Nova', 'Avaí', 'Amazonas FC', 'Coritiba',
          'Paysandu', 'Botafogo SP', 'Chapecoense', 'CRB',
          'Ponte Preta', 'Ituano', 'Brusque', 'Guarani')
número = 0

print('''TABELA BRASILEIRÃO SÉRIE B
DIGITE [1]: 5 PRIMEIROS COLOCADOS
DIGITE [2]: 4 ULTIMOS COLOCADOS
DIGITE [3]: TIMES EM ORDEM ALFABÉTICA
DIGITE [4]: EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE
DIGITE [5]: PARA FINALIZAR O PROGRAMA''')
print(f'TABELA DE TIMES: {tabela}')
while True:
    número = int(input('Digite um número: '))
    while número > 5:
        número = int(input('Tente novamente. Digite um número: '))
    if número == 1:
        print(f'Os 5 primeiros colocados são {tabela[0:5]}')
    if número == 2:
        print(f'Os 4 últimos colocados são: {tabela[-4:]}')
    if número == 3:
        print(f'Times em ordem alfabética: {sorted(tabela)}')
    if número == 4:
        print(f'O time de Chapecoense está na posição {len(tabela[:15])}ª.')
    if número == 5:
        break
print('PROGRAMA FINALIZADO!')



