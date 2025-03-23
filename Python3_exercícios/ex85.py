valores = [ [], []]
for valor in range(1,8):
    número = int(input(f'Digite o {valor}º valor: '))
    if número % 2 == 0:
        valores[0].append(número)
    else:
        valores[1].append(número)
valores[0].sort()
valores[1].sort()
print(f'O valores pares digitados foram: {valores[0]}')
print(f'E os valores impares foram: {valores[1]}')







