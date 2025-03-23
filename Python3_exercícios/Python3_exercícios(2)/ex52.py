primeirotermo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimotermo = primeirotermo + (10-1) * razão
for c in range(primeirotermo, decimotermo + razão, razão):
    print('{}'.format(c), end=' - ')
print('TERMINOU')