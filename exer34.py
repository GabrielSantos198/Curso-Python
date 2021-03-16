from time import sleep

print('\033[36m+\033[m'*39)
print('\033[34mA empresa fez um reajuste nos salários\033[m')
print('\033[36m+\033[m'*39)
valor = float(input('Digite seu salário e descubra o seu aumento: '))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if valor > 1250:
    print('Seu salário de R${:.2f} teve um aumento de 10% e agora você receberá R${:.2f}'.format(valor, valor+(valor*10/100)))
else:
    print('Seu salário de R${:.2f} teve um aumento de 15% e agora você receberá R${:.2f}'.format(valor, valor+(valor*15/100)))
print('\033[32mESPERO QUE VOCÊ TENHA GOSTADO DO AUMENTO\033[m')

