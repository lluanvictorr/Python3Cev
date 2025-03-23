def fatorial(n, mostrar=False):
      f = 1
      for c in range(n, 0, -1):
        if mostrar:
           print(f'{c}', end='')
           if c > 1:
            print(f' X ', end='')
           else:
             print(f' = {f}')
        f *= c
      return f


"""
--> Calcula o fatorial de um número.
:param num: O número a ser calculado
:param show: (opcional) Mostrar ou não a conta.
:return: O valor do Fatorial de um número num"""
num = int(input('Fatorial de qual número? '))
fatorial(num, mostrar=True)
print(f'\nO fatorial de {num} é {fatorial(num)}')

