from datetime import date

dados = {}
dados['nome'] = str(input('Digite seu nome: ')).strip()
nasc = int(input('Digite seu ano de nascimento: '))
dados['idade'] = (date.today().year) - nasc
ctps = int(input('Digite carteira de trabalho: '))
if ctps != 0:
    dados['ctps'] = ctps
    dados['contratacao'] = int(input('Digite seu ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: R$'))
    temp_trabalho = 35 - ((date.today().year) - dados['contratacao'])
    dados['aposentar'] = dados['idade'] + temp_trabalho
else:
    pass
print('-='*14)
for c,v in dados.items():
    print(f'{c}: {v}'.center(30))

