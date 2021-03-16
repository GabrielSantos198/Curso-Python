print('')
print('\033[1;35;46mCOMPARAÇÃO NUMERICA\033[m'.center(60))
print('')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O Primeiro valor é o  maior')
elif num1 < num2:
    print('O Segundo valor é o maior')
else:
    print('{} e {} são iguais'.format(num1, num2))

