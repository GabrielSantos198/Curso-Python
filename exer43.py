from time import sleep


print('\033[34m=\033[m'*35)
print('CALCULE SEU IMC'.center(35))
print('\033[34m=\033[m'*35)

peso = float(input('Quanto você pesa? '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura*altura)
print('\033[1;35mCalculando...\033[m')
sleep(2)
print('Seu IMC (Indice de Massa Corporal) deu {:.2f} Kg/m² e '.format(imc), end='')
if imc < 18.5:
    print('você está Abaixo do peso')
elif imc < 25:
    print('você está no peso Ideal')
elif imc <= 30:
    print('você está com Sobrepeso')
elif imc <= 40:
    print('você está com Obesidade')
else:
    print('você está com Obesidade Mórbida')


