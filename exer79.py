nums = []
while True:
    num = int(input('Digite um número: '))
    if num not in nums:
        nums.append(num)
        print('\033[32mValor adicionado com sucesso...\033[m')
    else:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')
    while True:
        continuar = str(input('Você quer continuar? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('\033[31mOpcão invalida. Digite novamente\033[m')
    if continuar == 'N':
        break
nums.sort()
print(nums)
