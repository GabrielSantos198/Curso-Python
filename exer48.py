s = 0
cont = 0
for c in range(1,501):
    if c%2 == 1 and c%3 == 0:
        s += c
        cont += 1
print('A soma entre todos os {} números Inpares multiplos de 3 é igual a {}'.format(cont,s))
        
