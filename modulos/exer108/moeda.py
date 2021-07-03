def aumentar(num):
    return num+(num*10/100)


def dobrar(num):
    return num*2


def diminuir(num):
    return num-(num*13/100)


def metade(num):
    return num/2


def moeda(num):
    return f'R${num:.2f}'.replace('.',',')
