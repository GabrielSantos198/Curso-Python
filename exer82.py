nums = []
impar = []
par = []
while True:
    nums.append(int(input('Digite um valor: ')))
    while True:
        res = str(input('Você quer conituar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção inválida digite novamente.\033[m')
    if res == 'N':
        break
for c in nums:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print('-='*13)
print(f'Os NÚMEROS digitados foram {nums}')
print(f'Os números PARES digitados foram {par}')
print(f'Os número IMPARES digitados foram {impar}')

