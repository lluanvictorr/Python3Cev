from cadastro.lib.interface import *
from time import sleep
from cadastro.lib.arquivo import *
arquivo = 'projectR.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)
    print(arquivo)

while True:
    resposta = menu(['LISTA DE CADASTRO','CADASTRAR USUÁRIO', 'SAIR'])
    if resposta == 1:
        # Opção de listagem de counteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        # Opção para cadastrar um novo usuário
        cabeçalho('NOVO USUÁRIO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        sleep(2)
        break

    else:
        print('ERRO! Digite uma opção válida!')
    sleep(1.5)
print('Certo. Até a próxima!')

