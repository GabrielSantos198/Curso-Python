import math
angulo = int(input('Digite um ângulo: '))
ra = math.radians(angulo)
print('O SENO DE {} É {:.2f}'.format(angulo, math.sin(ra)))
print('O COSSENO DE {} É {:.2f}'.format(angulo, math.cos(ra)))
print('A TANGENTE DE {} É {:.2f}'.format(angulo, math.tan(ra)))


