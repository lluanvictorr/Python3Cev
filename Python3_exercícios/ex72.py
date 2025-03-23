contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte',)

while True:
        número = int(input('Digite um número entre 0 e 20: '))
        if 0 < número > 20:
            print('Tente novamente. ',end='')
        else:
            print(f'Foi digitado o número {contagem[número]}!')
        pergunta = ''
        pergunta = str(input('Quer continuar? [S/N]')).upper()
        while pergunta not in 'SN':
            pergunta = str(input('Quer continuar? [S/N]')).upper()
        if pergunta == 'N':
            break
print('FIM!')







