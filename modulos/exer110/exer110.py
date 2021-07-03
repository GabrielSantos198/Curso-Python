import moeda

num = float(input('Digite algum valor: R$'))
print('-'*30)
print(f'{"RESUMO DO VALOR":^30}')
print('-'*30)
moeda.resumo(num)
print('-'*30)

