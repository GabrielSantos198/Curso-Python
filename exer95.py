dados = {}
lista = []
while True:
    dados['jogador'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    dados['gols'] = []
    for c in range(0,partidas):
        gols = int(input(f'Quantos gols {dados["jogador"]} fez na {c+1}ª partida? '))
        dados['gols'].append(gols)
    dados['total'] = sum(dados['gols'])
    lista.append(dados.copy())
    dados.clear()
    while True:
        res = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[1;31mA opção digitada é invalida. Digite S u N.\033[m')
    if res == 'N':
        break
    print('-'*30)
print('-='*20)
print(f'{"cod":<7}{"nome":<13}{"gols":<15}{"total"}')
print('-='*20)
for c,v in enumerate(lista):
    print(f'{c:<7}{v["jogador"]:<13}{str(v["gols"]):<15}{v["total"]}')
while True:
    print('-'*30)
    while True:
        cod = int(input('Você quer ver os dados de qual jogador? [999 PRA PARAR] '))
        if cod < len(lista) or cod == 999:
            break
        print('\033[1;31mJogador inexistente. Por favor digite novamente.\033[m')
    if cod == 999:
        break
    print(f'    -- LEVANTAMENTO DO JOGADOR {lista[cod]["jogador"]}:')
    for c,v in enumerate(lista[cod]["gols"]):
        print(f'           No jogo {c} fez {v} gols')


