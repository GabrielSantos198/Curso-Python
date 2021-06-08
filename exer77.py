palavras = ('CADEIRA','PORTA','PAREDE','ANTENA','PNEU','PESSOA','SONHO','PESADELO')
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos: ', end='')
    for i in range(0, len(palavras[c])):
        if palavras[c][i] in 'AEIOU':
            print(palavras[c][i], end='')
            
