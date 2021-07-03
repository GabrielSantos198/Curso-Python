def titulo(msg):
    print('-'*40)
    print(f'{msg:^40}')
    print('-'*40,end='')


def cadastros():
    try:
        abrir = open('file.txt','r')
    except:
        print('\033[33mNão ha nem uma Pessoas cadastrada no Sistema\033[m')
    else:
        titulo('PESSOAS CADASTRADAS')
        ler = abrir.readlines()
        print()
        nomes = []
        idades = []
        for c in range(0,len(ler)):
            if c % 2 == 0:
                nomes.append(f'{ler[c]}'.replace('\n',' '))
            else:
                idades.append(f'{ler[c]}'.replace('\n',' '))
        for c in range(0,len(nomes)):
            print(f'{nomes[c]:<30}{idades[c]}anos')


def novo():
    titulo('NOVO CADASTRO')
    print()
    while True:
        try:
            nome = str(input('Nome: ')).strip()
        except:
            print('\033[1;31mErro: Por favor digite algo valido\033[m')
        else:
            break
    if nome.isnumeric() or len(nome) == 0:
        nome = 'Desconhecido'
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[1;31mErro: Por favor digite uma idade valida.\033[m')
        else:
            abrir = open('file.txt','a')
            abrir.write(f'{nome}\n{idade}\n')
            break
    


