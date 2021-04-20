maior=menor=0
for c in range(1,6):
    peso = float(input('Qual o peso da {}° Pessoa: kg '.format(c)))
    if c == 1:
        maior=menor=peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('\033[35mO maior peso foi {} kg\033[m'.format(maior))
print('\033[36mO menor peso foi {} kg\033[m'.format(menor))

