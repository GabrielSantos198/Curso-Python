numeros = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE',
        'OITO','NOVE','DEZ','ONZE','DOZE','TREZE','CATORZE','QUINZE',
        'DESESSEIS','DESESSETE','DEZOITO','DEZENOVE','VINTE')

while True:
    while True:
        usuario = int(input('Digite um Numero [0/20] '))
        if usuario <= 20 and usuario >= 0:
            break
        else:
            print('\033[1;31mTente Novamente\033[m')
    print(numeros[usuario])
    while True:
        opcao = str(input('Você quer continuar? ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('\033[1;31mOpção inválida\033[m')
    if opcao == 'N':
        break


