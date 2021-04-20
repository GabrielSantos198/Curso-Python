print('{:=^40}'.format('PROGRESSÃO ARITIMÉTICA'))
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 0
while cont != 10:
    print(termo, end=' -> ')
    termo = termo+razao
    cont += 1
print('Fim')
