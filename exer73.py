times = ('SAO PAULO','INTERNACIONAL','ATLETICO-MG','FLAMENGO','GREMIO','PALMEIRAS',
        'FLUMINENSE','SANTOS','CORINTHIANS','ATLETICO-PR','CEARA','ATLETICO-GO',
        'BRAGANTINO','SPORT','FORTALEZA','VASCO','BAHIA','GOIAS','BOTAFOGO','CORITIBA')
print('-='*60)
print('Lista de times do Brasileirão: {}'.format(times))
print('-='*60)
print('Os 5 primeiros são {}'.format(times[:5]))
print('-='*60)
print('Os 4 últimos são {}'.format(times[-4:]))
print('-='*60)
print('Times em ordem alfabetica {}'.format(sorted(times)))
print('-='*60)
print('O Santos esta na {}ª posição'.format(times.index('SANTOS')+1))
print('-='*60)

