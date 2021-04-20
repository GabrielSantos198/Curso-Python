''''
num = int(input('Digite um número: '))
cont = 1
for c in range(num,0,-1):
    cont = cont*c
    if c != 1:
        print(c,end=' x ')
    else:
        print('1 = {}'.format(cont))
'''

num = int(input('Digite um número: '))
calc = 1
while num != 0:
    if num != 1:
        print(num, end=' x ')
    else:
        print('1 = {}'.format(calc))
    calc = calc*num
    num = num- 1

