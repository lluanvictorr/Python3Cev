ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota:'))
    nota2 = float(input('Segunda nota: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    pergunta = ' '
    pergunta = str(input('Quer continuar? [S/N] '.upper()))
    while pergunta not in 'SN':
     pergunta = str(input('Quer continuar? [S/N] '.upper()))
    if pergunta == 'N':
        break

print('-='*25)
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
print('=-'*25)
for número, aluno in enumerate(ficha):
    print(f'{número:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opção = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opção == 999:
        break
    if opção <= len(ficha) -1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('Obrigado, volte sempre!')

