def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except KeyboardInterrupt:
            print('O usuário decidiu não informar nem um valor')
            return 0
        except:
            print('Erro: Por favor digite um Inteiro Valido')
        else:
            return n


def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except KeyboardInterrupt:
            print('O usuário decidiu não informar nem um valor')
            return 0
        except:
            print('Erro: Por favor digite um Real Valido')
        else:
            return f'{n:.2f}'.replace('.',',')


