from time import sleep

def pular():
    print('')

# Titulo do Programa
pular()
print('#'*53)
print('\033[32m   APROVAÇÃO DE UM EMPRESTIMO BANCÁRIO   \033[m'.center(60, '#'))
print('#'*53)
pular()

valor_casa = float(input('Qual o valor da casa que você deseja comprar? R$'))
salario = float(input('Quanto você ganha de salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
print('\033[1;33mAVALIANDO...\033[m')
sleep(3)
prestacao = valor_casa/(12*anos)
if prestacao > salario*30/100:
    print('\033[31mSinto muito, mas o  emprestimo foi negado.\033[m')
else:
    print('\033[32mSua solicitação de emprestimo foi aceita.\033[m')
print('\033[35mVolte Sempre.\033[m')
