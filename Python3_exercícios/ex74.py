from random import randint
números = (randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5))
print('Os números sorteados foram: ')
for n in números:
    print(f'[{n}]', end='')
print(f'\nO maior número sorteado foi {max(números)}',end='')
print(f'\nO menor número sorteado foi {min(números)}.',end='')