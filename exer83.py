tup = []
tup2 = []
expressao = str(input('Digite uma expressao: '))
for c in range(0,len(expressao)):
    if expressao[c] in '(':
        tup.append(c)
    elif expressao[c] in ')':
        tup2.append(c)
if len(tup) == len(tup2):
    cont = 0
    acertos = 0
    while  cont < len(tup):
        if tup[cont] < tup2[cont]:
            acertos += 1
        cont += 1
    if cont == acertos:
        print('EQUACAO CORRETA')
    else:
        print('EQUACAO INCORRETA')
else:
    print('EQUACAO INCORRETA')

