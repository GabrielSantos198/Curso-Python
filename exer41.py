from datetime import date


nasc = int(input('Digite seu ano de nascimento: '))
idade = (date.today().year)-nasc
if idade <= 9:
    print('Você tem {} anos e sua categoria no campeonato é Mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e sua categoria no campeonato é Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e sua categoria no campeonato é Junior.'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e sua categoria no campeonato é Sênior.'.format(idade))
else:
    print('Você tem {} anos e sua categoria no campeonato é Master.'.format(idade))

