somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totalmulher20 = 0
for pessoas in range(1, 5):
    print('------- {}º PESSOA -------'.format(pessoas))
    nome =str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M] ou [F]: '))
    somaidade = somaidade + idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
      totalmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade deste grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomemaisvelho))
print('O total de mulheres com menos de 20 anos é {}.'.format(totalmulher20))