listadevalores = []
for c in range(0, 5):
   novovalor = int(input('Digite um valor: '))
   if c == 0 or novovalor > listadevalores[-1]:
    listadevalores.append(novovalor)
    print('Adicionado ao fim da lista!')
   else:
        posição = 0
        while posição < len(listadevalores):
            if novovalor <= listadevalores[posição]:
                listadevalores.insert(posição, novovalor)
                print(f'Adicionado na posição {posição+1} da lista')
                break
            posição += 1
print(f'Os valores informados foram: {listadevalores}')
