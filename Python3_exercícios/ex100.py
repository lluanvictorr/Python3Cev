from random import randint
from time import  sleep
def sorteia(lista):
    print('Sorteando 5 números...')
    sleep(1.5)
    for n in range(0, 5):
     sorteio = randint(1, 10)
     lista.append(sorteio)
     print(f'{sorteio} ', end='')



def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'. Somando os valores pares sorteados o resultado é {soma}.')


números = list()
sorteia(números)
somapar(números)
print('\n<<< FIM >>>')


