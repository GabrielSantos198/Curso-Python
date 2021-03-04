from random import choice
a1 = str(input('NOME DO PRIMEIRO ALUNO: '))
a2 = str(input('NOME DO SEGUNDO ALUNO: '))
a3 = str(input('NOME DO TERCEIRO ALUNO: '))
a4 = str(input('NOME DO QUARTO ALUNO: '))
alunos = a1, a2, a3, a4
print('O sorteado foi {}'.format(choice(alunos)))

