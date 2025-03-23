def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um númeiro inteiro válido!')
            continue
        except KeyboardInterrupt:
            print(f'O usuário não quis digitou !')
            return 0
        else:
            return valor


def linha(tamanho = 40):
    return '-=' * tamanho


def cabeçalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc