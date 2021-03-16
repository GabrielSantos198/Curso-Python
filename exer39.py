from datetime import  date
from time import sleep


print('')
print('\033[1;32mSERVIÇO MILITAR\033[m'.center(60))
print('')
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year-nasc
print('\033[33mAnalisando...\033[m')
sleep(3)
if idade < 18:
    print('\033[1;33mAinda falta {} anos pra você pode se alistar\033[m'.format(18-idade))
elif idade == 18:
    print('\033[1;32mJá tá na hora de você se alistar\033[m')
else:
    print('\033[1;31mPassou {} anos do tempo de você se alistar e terá que pagar uma multa de R$5.00\033[m'.format(idade-18))
# Nota
sleep(4)
print('')
print('\033[34m-=\033[m'*24)
print('\033[33mNOTA:\033[m O alistamento militar é obrigatório quando o homem atingi a fase adulta que no Brasil é aos 18 anos')
sleep(7)
print('')
print('Se você não se alistar não podera trabalhar ou fazer viajens internacionais, para fazer seu alistamento acesse o site www.alistamento.br ou vá até a junta de serço militar mais próxima da sua casa')
sleep(7)
print('')
print('Se você passou do tempo de alistamento devera ir até ajunta de serço militar e faze-ló além de também ter que pagar uma multa')
sleep(5)
print('')
print('Obrigado por usar nosso app')
print('\033[34m-=\033[m'*24)
