numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total = total + 1
        print('\033[32m', end=' ')
        print('{}'.format(c), end=' ')
    else:
        print('\033[33m', end=' ')
        print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(numero, total))
if total == 2:
    print('E por isto ELE É um NÚMERO PRIMO!')
else:
    print('\033[31m''Ele NÃO É um NÚMERO PRIMO!')


