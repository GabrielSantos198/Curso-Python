lista = []
while True:
    nome = str(input('Digite seu Nome: ')).strip()
    nota1 = float(input('Digite sua Primeira Nota: '))
    nota2 = float(input('Digite sua Segunda Nota: '))
    media = (nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    while True:
        res = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção invalida. Digite Novamente.\033[m')
    if res == 'N':
        break

print('\033[34m-=\033[m'*14)
print('BOLETIM'.center(30))
print('\033[34m-=\033[m'*14)
print('{:<10}{:<10}{:<10}'.format("NÚMEROS","ALUNOS","MEDIAS"))
print('\033[33m~\033[m'*28)

for c in range(0,len(lista)):
    print('{:<10}{:<10}{:<10.1f}'.format(c,lista[c][0], lista[c][2]))
print('\033[33m~\033[m'*28)

while True:
    while True:
        res = str(input('Você quer vê as notas de algum aluno especifico? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        print('\033[31mOpção invalida. Digite Novamente.\033[m')
    if res == 'N':
        break
    while True:
        aluno = int(input('Qual o número do Aluno? '))
        if aluno < len(lista):
            break
        print('\033[31mAluno não existe. Digite Novamente.\033[m')
    print('\033[33m~\033[m'*28)
    print(f'O aluno {lista[aluno][0]} obteve as seguintes notas: {lista[aluno][1]}')
    print('\033[33m~\033[m'*28)
