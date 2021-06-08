nums = []
for c in range(0,5):
    num = int(input(f'Digite o {c} valor: '))
    if c == 0 or num > nums[c-1]:
        nums.append(num)
        print('\033[32mAdicionado ao final da lista...\033[m')
    else:
        c = 0
        while nums[c] < num:
            c+=1
        nums.insert(c,num)
        print(f'\033[32mAdicionado na posicao {c} da lista...\033[m')
print(nums)
