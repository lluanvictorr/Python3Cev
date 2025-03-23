print('GERADOR DE PROGRESSÃO ARITMÉTICA')
print('='* 40)
primeirotermo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeirotermo
contador = 1
while contador <= 10:
    print('{} - '.format(termo), end='')
    termo += razão
    contador += 1
print('FIM')
