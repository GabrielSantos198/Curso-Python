print('-='*20)
print('Radar Eletrônico'.center(40))
print('-='*20)
velocidade = int(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('\033[32mVocê pode seguir em frente.\033[m')
else:
    print('\033[31mVocê ultrapassou o limite de velocidade e foi multado em {:.2f} R$ \033[m'.format((float(velocidade-80)*7)))

