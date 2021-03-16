soma = 0
for c in range(0,6):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num%2 == 0:
        soma += num
print('A soma de todos os números Pares digitados foi {}'.format(soma))

