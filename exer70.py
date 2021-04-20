from datetime import date
from time import sleep

# Título
print('{:^40}'.format('='*20))
print(f'{" ANÁLISE DE DADOS ":^40}')
print('{:^40}'.format('='*20))

tot = mais_de_mil = cont = menor = produto = 0
while True:
    cont += 1
    nome = str(input('Digite o nome do Produto: ')).strip()
    preco = float(input('Quanto custa esse Produto? R$'))
    if cont == 1:
        produto = nome
        menor = preco
    else:
        if preco < menor:
            menor = preco
            produto = nome
    if preco > 1000:
        mais_de_mil += 1
    tot += preco
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('\033[1;31mError digite SIM ou NÃO \033[m')
    if continuar == 'N':
        break

# Resultado Final
print('\033[1;32mAnalisando...\033[m')
sleep(2)
print('-='*20)
print(f'\033[1;37mO total gasto na compra foi R${tot:.2f} Reais')
print(f'{mais_de_mil} Produtos custam mais de R$1000.00 Reais')
print(f'O produto mais barato foi o {produto} que custou R${menor:.2f} Reais\033[m')
print('Analise feita em {}'.format(date.today()))
print('-='*20)

