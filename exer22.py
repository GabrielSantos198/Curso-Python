nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculo >>> {}'.format(nome.upper()))
print('Seu nome em minúsculo >>> {}'.format(nome.lower()))
separar = nome.split()
juntar = ''.join(separar)
print('Seu nome tem {} letras sem considerar os espaços'.format(len(juntar)))
print('O primeiro nome tem {}'.format(len(separar[0])))

