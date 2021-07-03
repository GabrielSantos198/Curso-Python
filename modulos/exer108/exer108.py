import moeda
from time import sleep

num = float(input('Digite algum valor: R$'))
print('\033[33mAnalisando...\033[m')
sleep(2)
print('-'*30)
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobrar(num))}')
print(f'{moeda.moeda(num)} MAIS 10% de seu valor é {moeda.moeda(moeda.num(num))}')
print(f'{moeda.moeda(num)} MENOS 13% de seu valor é {moeda.moeda(moeda.diminuir(num))}')
print('-'*30)
