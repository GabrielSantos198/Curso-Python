n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
continuar = True
while continuar == True:
    print(''' 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Valores
    [ 5 ] Sair
    ''')
    opcao = int(input('>>> Qual sua Opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('O resultado de {} X {} deu {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        print('O maior número digitado foi {}'.format(max(n1,n2)))
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        continuar = False
    else:
        print('\033[1;31mEssa opcão não existe.\033[m')
    print('=-='*10)
print('\033[1;37mFim do Programa.\033[m')


