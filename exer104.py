def leiaint(entrada):
    while True:
        num = str(input(entrada))
        if num.isnumeric():
            return int(num)
            break
        print(f'\033[31m{num} não é um valor numérico. Por Favor digite novamente.\033[m')


num = leiaint('Digite um número: ')
print(num)

