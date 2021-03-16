distancia = float(input('Qual a distancia da viajem em km? '))
if distancia <= 200:
    print('A passagem custou {:.2f} R$'.format(distancia*0.50))
else:
    print('A passagem custou {:.2f} R$'.format(distancia*0.45))

