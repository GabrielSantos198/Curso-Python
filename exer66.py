# Titulo do Programa
print()
print(f'{"DIGITE 999 PRA PARAR":-^40}')
print()

s = c = 0
while True:
    núm = int(input('Digite um número: '))
    if núm == 999:
        break
    c += 1
    s += núm
print(f'\033[1;37mA soma dos {c} números digitados foi {s}\033[m')

