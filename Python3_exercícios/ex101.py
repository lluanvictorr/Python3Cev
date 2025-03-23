

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade > 70:
        print(f'Você tem {idade} anos, acima de 70 anos seu voto NÃO É MAIS OBRIGATÓRIO!')
    elif idade < 16:
        return f'Você tem {idade} anos. NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos, seu VOTO É OPCIONAL'
    else:
        return f'Sua idade é {idade} anos, apartir dos 18 anos seu VOTO É OBRIGATÓRIO!'

#ProgramaPrincipal
print('-='*30)
anonascimento = int(input('Ano que você nasceu: '))
print('-='*30)
print(voto(anonascimento))

