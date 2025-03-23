aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média do aluno(a) {aluno["nome"]} : '))
if aluno['média'] >= 7:
    aluno['resultado'] = 'Aprovado(a)'
elif 5 <= aluno['média'] < 7:
    aluno['resultado'] = 'Recuperação'
else:
    aluno['resultado'] = 'Reprovado(a)'
for key, valor in aluno.items():
    print(f'{key} é {valor}')
