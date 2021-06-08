valores = (int(input('Digite um valor: ')), 
        int(input('Digite um valor: ')), 
        int(input('Digite um valor: ')), 
        int(input('Digite um valor: '))
        )
print(f'Os números digitados foram: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'A primeira ocorrência de 3 foi na  {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números Pares digitados foram: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')

