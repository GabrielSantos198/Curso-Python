nums = [[],[]]
for c in range(1,8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print('='*30)
nums[0].sort() 
nums[1].sort()
print(f'Os valores PARES digitados foram {nums[0]}')
print(f'Os valores  ÍMPARES digitados foram {nums[1]}')


