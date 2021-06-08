dados = {}
dados['nome'] = str(input('Digite seu nome: ')).strip()
dados['media'] = float(input(f'{dados["nome"]} digite sua media: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif dados['media'] < 7:
    dados['situacao'] = 'Reprovado'
print(f'O aluno {dados["nome"]} cuja media foi {dados["media"]} foi {dados["situacao"]}')
