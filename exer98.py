from time import sleep

def contador(inicio,fim,passo):
    if passo < 0:
        trans = str(passo)
        t = trans[1:]
        passo = int(t)
    elif passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}')
    sleep(1.5)
    if inicio < fim:
        for c in range(inicio,fim+1,passo):
            print(c,end=' ',flush=True)
            sleep(.5)
        print('<FIM>!')
    elif inicio > fim:
        for c in range(inicio,fim-1,-passo):
            print(c,end=' ',flush=True)
            sleep(.5)
        print('<FIM>!')
    print('-='*20)


contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem.')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))

