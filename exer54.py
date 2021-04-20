from datetime import date

atual = date.today().year
menor = maior = 0
for c in range(1,8):
    ano = int(input('Ano de nascimento da {}° pessoa: '.format(c)))
    if atual-ano < 18:
        menor += 1
    else:
        maior += 1
print('\033[1;34m{} pessoas ainda são de menores\033[m'.format(menor))
print('\033[1;32m{} pessoas são de maior\033[m'.format(maior))

