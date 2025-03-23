print('='*25)
print('      BANCO CIDADÃO')
print('='*25)
saque = int(input('Qual valor você quer sacar? R$'))
valorsaque = saque
cédulabanco = 200
totalcédula = 0
while True:
    if valorsaque >= cédulabanco:
       valorsaque -= cédulabanco
       totalcédula += 1
    else:
        if totalcédula > 0:
         print(f'{totalcédula} cédulas de R${cédulabanco}')
        if cédulabanco == 200:
            cédulabanco = 100
        if cédulabanco == 100:
            cédulabanco = 50
        if cédulabanco == 50:
            cédulabanco = 20
        elif cédulabanco == 20:
            cédulabanco = 10
        elif cédulabanco == 10:
                cédulabanco = 1
        totalcédula = 0
        if valorsaque == 0:
            break
print('='*30)
print('VOLTE SEMPRE! O BANCO CIDADÃO AGRADECE SUA PREFERÊNCIA!')
