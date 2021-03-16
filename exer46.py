from time import sleep


print('\033[32m-=\033[m'*20)
print('\033[1;34;43mCONTAGEM REGRESSÍVA DE FIM DE ANO\033[m'.center(50))
print('\033[33m-=\033[m'*20)

for c in range(10,-1,-1):
    sleep(1)
    print('\033[1;35m{}\033[m'.format(c))
print('\033[1;32mFELIZ ANO NOVO, \033[m \033[31mBum\033[m \033[32mbumm\033[m \033[33mpuff\033[m \033[34mpraa\033[m \033[35mbum ....\033[m')

