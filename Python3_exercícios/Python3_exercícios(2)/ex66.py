print('-' * 20)
print('CÁLCULO DE MÉDIA')
print('-' * 20)
resposta = 'S'
soma = quantidade = média = maior = menor = 0
while resposta in 'Ss':
    número = int(input('Digite um número: '))
    soma += número
    quantidade += 1
    if quantidade == 1:
        maior = menor = número
    else:
        if número > maior:
         maior = número
        if número < menor:
            menor = número
    resposta = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
média = soma / quantidade
print('Você digitou {} números, e a média disto tudo foi {}.'.format(quantidade, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))





