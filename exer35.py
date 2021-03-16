from time import sleep

print('\033[35m#\033[m'*42)
print('\033[43;31mDESCUBRA SE AS RETAS FORMAM UM TRIÂNGULO.\033[m')
print('\033[35m#\033[m'*42)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print('\033[33mCALCULANDO...\033[m')
sleep(2)
menor = min(r1, r2, r3)
maior = max(r1, r2, r3)
meio = (r1+r2+r3) - (maior+menor)
soma = menor+meio
if soma > maior:
    print('\033[32mCom esses comprimentos de retas é possível formar um triângulo.\033[m')
else:
    print('\033[31mCom esses comprimentos de retas não foi possível formar um triângulo.\033[m')

