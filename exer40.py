from time import sleep

print('-='*24)
print('CALCULE SUA MÉDIA'.center(46))
print('-='*24)

n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
media = (n1+n2)/2
print('\033[1;36mCalculando...\033[m')
sleep(3)
if media < 5:
    print('\033[1;31mSua média foi {:.1f} e Você foi reprovado, estude mais na próxima vez.\033[m'.format(media))
elif media >= 5 and  media <= 6.9:
    print('\033[1;33mSua média foi {:.1f} e Você esta na recuperação.\033[m'.format(media))
else:
    print('\033[1;32mSua média foi {:.1f} Parabéns você foi Aprovado.\033[m'.format(media))

