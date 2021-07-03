def ficha(nome, gols):
    if len(nome) == 0:
        nome = 'Desconhecido'
    if len(gols) == 0:
        gols = 0
    print(f'O jogador {nome} fez {gols} Gols no campeonato')


ficha(str(input('Digite o nome do Jogador: ')),
       input('Qual a quantidade de gols do Jogador? '))

