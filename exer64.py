num = cont = somar = 0
while num != 999:
    cont += 1
    num = int(input(f'Digite o {cont}° número: \033[1;37m999 é a condição de parada\033[m '))
    somar += num
print('~'*40)
print(f'Você digitou {cont-1} números e a soma de todos deu {somar-999}')

