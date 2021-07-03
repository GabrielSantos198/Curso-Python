def aumentar(num,value=False):
    if value == True:
        formatado = moeda(num+(num*10/100))
        return formatado
    else:
        return num+(num*10/100)


def dobrar(num,value=False):
    if value == True:
        formatado = moeda(num*2)
        return formatado
    else:
        return num*2


def diminuir(num,value=False):
    if value == True:
        formatado = moeda(num-(num*13/100))
        return formatado
    else:
        return num-(num*13/100)


def metade(num,value=False):
    if value == True:
        formatado = moeda(num/2)
        return formatado
    else:
        return num/2


def moeda(num):
    return f'R${num:.2f}'.replace('.',',')


def resumo(num):
    resultados = {}
    resultados['Preço analisado:'] = moeda(num)
    resultados["Dobro do peso:"] = dobrar(num,True)
    resultados["Metade do preço:"] = metade(num,True)
    resultados["10% de aumento:"] = aumentar(num,True)
    resultados["13% de diminuição:"] = diminuir(num,True)
    for c,v in resultados.items():
        print(f'{c:<22}{v}')

