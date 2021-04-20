print('\033[35m-=\033[m'*20)
print('\033[33mCAIXA ELETRÔNICO\033[m'.center(45))
print('\033[35m-=\033[m'*20)

sacar = int(input('QUANTO VOCÊ DESEJA SACAR? R$'))
calc = sacar//50
sacar = sacar-(calc*50)
calc1 = sacar//20
sacar = sacar-(calc1*20)
calc2 = sacar//10
sacar = sacar-(calc2*10)
calc3 = sacar//1
sacar = sacar-(calc3*1)
if calc != 0:
    print('Total de {} cédulas de R$50,00 Reais'.format(calc))
if calc1 != 0:
    print('Total de {} cédulas de R$20,00 Reais'.format(calc1))
if calc2 != 0:
    print('Total de {} cédulas de R$10,00 Reais'.format(calc2))
if calc3 != 0:
    print('Total de {} moedas de R$1,00 Reais'.format(calc3))
print('\033[35m-=\033[m'*20)
