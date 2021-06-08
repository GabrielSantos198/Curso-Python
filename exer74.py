from random import randint

nums = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Números Gerados: ', end='')
for c in nums:
    print(c, end=' ')
print(f'\nO menor valor da Tupla é {min(nums)}')
print(f'O maior valor da Tupla é {max(nums)}')




