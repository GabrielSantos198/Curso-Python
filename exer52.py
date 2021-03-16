print('\033[35m=\033[m'*20)
print('\033[1;36m{:^20}\033[m'.format('NÚMERO PRIMO'))
print('\033[35m=\033[m'*20)

tot = 0
num = int(input('Digite um número: '))
for c in range(1,num+1):
    if num%c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[m{} é um número Primo'.format(num))
else:
    print('\n\033[m{} não é um número Primo'.format(num))
    
