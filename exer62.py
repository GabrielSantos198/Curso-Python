print('\033[34m-=\033[m'*20)
print('{:^50}'.format('\033[1;33mPROGRESSÃO ARITIMÉTICA\033[m'))
print('\033[34m-=\033[m'*20)

termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
c = 10
cont = 0
while c != 0:
    print(termo,'->',end=' ')
    termo += razao
    cont += 1
    if cont == c:
        print('PAUSA')
        c = int(input('\nQuantos termos você ainda quer ver? Digite 0 pra parar '))
        cont = 0
print('\033[1;37mFim\033[m')

