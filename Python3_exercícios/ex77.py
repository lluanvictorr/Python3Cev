palavras = (str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')),
            str(input('Digite uma palavra: ')))
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
