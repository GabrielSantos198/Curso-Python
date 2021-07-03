def maior(*nums):
    print('-='*20)
    print('Valores passados: ',nums)
    print(f'Foram digitados ao todo: {len(nums)} números.')
    p = 0
    for c,v in enumerate(nums):
        if c == 0:
            p = v
        else:
            if v > p:
                p = v
    print('O maior número digitado foi',p)


maior(2,4,5,6,9,0)
maior(12,3,4,6)
maior()
