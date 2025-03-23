from cadastro.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('USUÁRIOS CADASTRADOS')
        for linha in a:
           dado = linha.split(',')
           dado[1] = dado[1].replace('\n', '')
           print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro na execução do arquivo!')
    else:
        try:
            a.write(f'{nome}, {idade}\n')
        except:
            print('Houve um ERRO ao inserir os dados!')
        else:
            print(f'Novo usuário adicionado! {nome}.')
        a.close()
