def área(largura, comprimento):
    áreaterreno = largura * comprimento
    print(f'A área do terreno de {largura}x{comprimento} é de {áreaterreno}m². ')

print(f'{"MEDIDOR DE TERRENOS":>35}')
print('=-'*30)
l = float(input('Largura do terreno(m): '))
c = float(input('Comprimento do terreno(m): '))
área(l, c)


