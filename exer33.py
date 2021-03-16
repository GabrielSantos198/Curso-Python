num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite mais um número: '))
if num1 == num2 and num1 == num3:
    print('Todos os números são iguais, não há maior nem menor')
else:
    print('O maior número foi o {}'.format(max(num1, num2, num3)))
    print('O menor número foi o {}'.format(min(num1, num2, num3)))

