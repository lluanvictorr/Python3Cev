from time import sleep
total = 0
preçomaior = 0
preçomenor = 0
maisdemil = 0
totalproduto = 0
quantidade = 0
barato = ' '
print('-='* 20)
print('          AMERICANA MARKET')
print('-='* 20)

while True:
    nomeproduto = str(input('Informe o NOME do produto comprado: ')).upper()
    preçoproduto = float(input('Informe o PREÇO do produto comprado: R$'))
    quantidade += 1
    if quantidade == 1:
        preçomenor = preçoproduto
        barato = nomeproduto
    else:
        if preçoproduto < preçomenor:
            preçomenor = preçoproduto
            barato = nomeproduto
    if preçoproduto > 1000:
        maisdemil += 1
    total += preçoproduto
    totalproduto += 1
    resposta = ' '
    while resposta not in 'SN':
     resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if resposta == 'N':
            break
print(f'''TOTAL DE PRODUTOS: {totalproduto} 
TOTAL DA COMPRA: R${total :.2f} 
TOTAL DE PRODUTOS QUE CUSTARAM MAIS DE R$1000: {maisdemil} 
O PRODUTO MAIS BARATO FOI {barato} E CUSTOU R${preçomenor :.2f}''')
print('...')
sleep(1)
print('PROGRAMA FINALIZADO!')