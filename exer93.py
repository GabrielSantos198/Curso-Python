dados = {}
dados['jogador'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
dados['gols'] = []
for c in range(0,partidas):
    gols = int(input(f'Quantos gols {dados["jogador"]} fez na {c+1}ª partida? '))
    dados['gols'].append(gols)
dados['total'] = sum(dados['gols'])
print('-='*20)
print(dados)
print('-='*20)
for c,v in dados.items():
    print(f'O campo {c} tem valor {v}')
print('-='*20)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for c in range(0,partidas):
    print('{:>32}'.format(f'=> Na partida {c+1}, fez {dados["gols"][c]} gols.'))
print(f'Foi um total de {sum(dados["gols"])} Gols.')

