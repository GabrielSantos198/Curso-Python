print('-='*14)
print('CALCULE A ÁREA DO TERRENO'.center(28))
print('-='*14)

def area(l,c):
    print('='*30)
    print(f'A área do terreno {l}x{c} é de {l*c}m²')
    print('='*30)


area(float(input('Digite a largura do terreno: (m) ')),
        float(input('Digite o cumprimento do terreno: (m) ')))
print(f'{"<<< FIM DO PROGRAMA >>>":^30}')

