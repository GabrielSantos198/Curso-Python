print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
for c in range(termo,termo+(razao*10),razao):
    print(c, end=' -> ')
print('ACABOU')
