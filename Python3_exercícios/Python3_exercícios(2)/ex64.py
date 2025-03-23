print('~' * 40)
print('SEQUÊNCIA DE FIBONACCI')
print('~' * 40)
termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
contador = 3
print('~' * 40)
print('{} - {}'.format(t1, t2),end='')
while contador <= termos:
    t3 = t1 + t2
    print(' - {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' - FIM')
print('~' * 40)
