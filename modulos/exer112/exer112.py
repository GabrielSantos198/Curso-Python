from utilidadesCeV import moeda
from utilidadesCeV.dado import leiaDinheiro

num = leiaDinheiro('Digite algum valor: R$')
print('-'*30)
print(f'{"RESUMO DO VALOR":^30}')
print('-'*30)
moeda.resumo(num)
print('-'*30)

