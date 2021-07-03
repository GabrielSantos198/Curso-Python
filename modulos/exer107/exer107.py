import moeda

num = float(input('Digite algum valor: R$'))
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobrar(num)}')
print(f'{num} MAIS 10% de seu valor é {moeda.aumentar(num)}')
print(f'{num} MENOS 13% de seu valor é {moeda.diminuir(num)}')
