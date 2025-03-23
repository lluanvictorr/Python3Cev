from time import sleep
print('=-'*15)
print('MOSTRE-ME A TABUADA!')
print('=-'*15)
while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    print('Certo...')
    sleep(1.3)
    if n < 0:
        break
    print('=-'*15)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')

    print('=-' * 15)
print('MOSTRE-ME A TABUADA ENCERRADO'. Obrigado e volte sempre!')