matriz = [[],[],[]]
for c in range(0,3):
    for i in range(0,3):
        matriz[c].append(int(input(f'Digite um valor na posição {c, i} ')))
print('-='*14)
par = 0
for c in range(0,3):
    for i in range(0,3):
        if matriz[c][i] % 2 == 0:
            par += matriz[c][i]
        print(f'[ {matriz[c][i]:^5} ]',end=' ')
    print()
print('-='*14)
print(f'A soma de todos os valores PARES digitados foi {par}')
print(f'A soma de todos os valore da 3 Terceira coluna foi {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor digitado na linha 2 foi o {max(matriz[1])}')

