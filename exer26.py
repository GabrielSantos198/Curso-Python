frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra "A" aparece na frase {} vezes'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição {}'.format(frase.find('A')))
print('A letra "A" aparece por último na posição {}'.format(frase.rfind('A')))
