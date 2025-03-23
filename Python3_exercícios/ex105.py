def notas(*num, situação=False):
        nota = dict()
        nota['total'] = len(num)
        print(f'Total de notas {nota["total"]}.')
        nota['maior'] = max(num)
        print(f'A maior nota foi {nota["maior"]}.')
        nota['média'] = sum(num)/len(num)
        print(f'A média das notas foi {nota["média"]}')
        if situação:
            if nota['média'] > 7:
                nota['situação'] = 'BOA'
            elif nota['média'] >= 5:
                nota['situação'] = 'RAZOÁVEL'
            else:
                nota['situação'] = 'RUIM'
        return nota



resposta = notas(8, 8, 8, 8, situação=True)
print(resposta)


