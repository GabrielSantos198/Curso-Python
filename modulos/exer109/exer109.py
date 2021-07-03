import moeda
from time import sleep

num = float(input('Digite algum valor: R$'))
print('\033[33mAnalisando...\033[m')
sleep(2)
print('-'*30)
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num,True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobrar(num)}')
print(f'{moeda.moeda(num)} MAIS 10% de seu valor é {moeda.num(num,True)}')
print(f'{moeda.moeda(num)} MENOS 13% de seu valor é {moeda.diminuir(num,True)}')
print('-'*30)
