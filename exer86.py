matriz = [[0,0],[0,1],[0,2],
         [1,0],[1,1],[1,2],
         [2,0],[2,1],[2,2]]
for c in range(0,9):
    while True:
        num = int(input(f'Digite um número na posição {matriz[c]} '))
        if len(str(num)) <= 3:
            break
        print('\033[31mDigite um número menor do que 3\033[m')
    matriz[c].clear()
    matriz[c].append(num)
print(f"""
    {f'{matriz[0]}':<6} {f'{matriz[1]}':<6} {f'{matriz[2]}':<6}
    {f'{matriz[3]}':<6} {f'{matriz[4]}':<6} {f'{matriz[5]}':<6}
    {f'{matriz[6]}':<6} {f'{matriz[7]}':<6} {f'{matriz[8]}':<6}
""")

