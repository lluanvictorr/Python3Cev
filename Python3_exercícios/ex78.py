valores = []
maior = 0
menor = 0
for contador in range(0, 5):
     valores.append(int(input(f'Digite um número para a posição {contador}: ')))
     if contador == 0:
      maior = menor = valores[contador]
     else:
        if valores[contador] > maior:
            maior = valores[contador]
        if valores[contador] < menor:
            menor = valores[contador]
print(f'Você digitou os números {valores}')
print(f'O maior valor foi {maior}, nas posições ', end='')
for posição, valor in enumerate(valores):
    if valor == maior:
        print(f'{posição}.', end='')
print(f'\nE o menor valor foi {menor}, e está na posições ', end='')
for posição, valor in enumerate(valores):
    if valor == menor:
        print(f'{posição}.', end='')





