from time import sleep

nums = []
while True:
    nums.append(int(input('Digite um valor: ')))
    while True:
        res = str(input('Você quer continuar: [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção inválida digite novamente\033[m')
    if res == 'N':
        break
print('\033[35mAnalisando...\033[m')
sleep(2)
print('-='*14)
print(f'Foram digitados {len(nums)} números')
if 5 in nums:
    print(f'O número 5 existe na lista e está nas posicoes ', end=' ')
    for d,c in enumerate(nums):
        if c == 5:
            print(d, end=' ')
else:
    print('O número 5 nao foi digitado')
nums.sort(reverse=True)
print(f'\nOs valores em ordem decrescente {nums}')
