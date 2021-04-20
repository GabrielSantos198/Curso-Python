print('{:^60}'.format('\033[1;32;45mSEQUENCIA DE FIBONACCI\033[m'))
num = int(input('Quantos termos você quer ver? '))
cont = 0
c = 0
s = 1
while cont < num//2:
    cont+=1
    print(c,s,end=' ')
    c += s
    s += c
print('\n\033[1;37mFim\033[m')

