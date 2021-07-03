from random import randint

numeros = []

def sorteio():
    for c in range(0,5):
        numeros.append(randint(1,10))


def somaPar(lst):
    cont = 0
    for c in lst:
        if c % 2 == 0:
            cont += c
    print(f'A soma de todos os números PARES contidos na lista {numeros} deu {cont}')

sorteio()
somaPar(numeros)

