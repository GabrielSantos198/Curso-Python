nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('O seu primeiro nome é {}'.format(lista[0]))
comp = len(lista)-1
print('O seu último nome é {}'.format(lista[comp]))

