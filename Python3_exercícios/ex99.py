from time import sleep
def maior(* num):
        contador = maior = 0
        tamanho = len(num)
        print('Analisando valores informados...')
        sleep(1.5)
        for número in num:
            print(f'{número}', end=' ')
            sleep(0.5)
        print(f'. Ao todo {tamanho} números informados.')
        sleep(1.5)
        if contador == 0:
          maior = número
        else:
            if número >= maior:
                número = maior
        contador += 1
        print(f'E o maior valor é {maior}.')
        print('=-'* 25)
        sleep(0.5)

maior(10, 7, 3, 12, 56)
maior(67, 43, 33, 9, 80)
maior(1, 5, 20, 40)
maior(3, 6, 9)