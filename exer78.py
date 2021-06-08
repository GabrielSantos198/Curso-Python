from time import sleep

nums = []
for c in range(1, 6):
    nums.append(int(input(f'Digite o {c}ª valor: ')))
print('\033[33mANALISANDO...\033[m')
sleep(2)
print(f'Os números digitados foram {nums}')
maior = max(nums)
print(f'O maior numero digitado foi {maior} nas posições: ', end='')
for i,f in enumerate(nums):
    if f == maior:
        print(i+1, end='... ')
menor = min(nums)
print(f'\nO menor numero digitado foi {menor} nas posicoes: ', end='')
for i,f in enumerate(nums):
    if f == menor:
        print(i+1, end='... ')
print('\n')


