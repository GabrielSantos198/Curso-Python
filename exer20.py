import random

print('')
a1 = str(input('PRIMEIRO ALUNO: '))
a2 = str(input('SEGUNDO ALUNO: '))
a3 = str(input('TERCEIRO ALUNO: '))
a4 = str(input('QUARTO ALUNO: '))
alunos = (a1, a2, a3, a4)
embaralhar = random.sample(alunos, k=4)
print('')
print('ESSA É A ORDEM DOS SORTEADOS: ')
print('')
cont = 1
for c in embaralhar:
    print(cont, c)
    cont += 1
print('')

