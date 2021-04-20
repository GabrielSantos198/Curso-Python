stop = False
cont = media = 0
maior = 0
menor = 0
while stop == False:
    num = int(input('Digite um número: '))
    media += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    continua = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SsNn':
        print('\033[1;31mEROR: Digite uma opção válida!\033[m')
        continua = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        stop = True
    else:
        pass
print('A media de todos os números digitados foi {:.2f}'.format(media/cont))
print('Entre todos os números digitados o maior foi {} e o menor foi {}'.format(maior, menor))

