from datetime import date
print('\033[33m#\033[m'*30)
print('DESCUBRA SE O ANO É BISSEXTO')
print('\033[33m#\033[m'*30)
ano = int(input('Qual ano você deseja analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0:
    print('\033[32m{} é um ano Bissexto \033[m'.format(ano))
else:
    print('\033[31m{} não é um ano Bissexto\033[m'.format(ano))

