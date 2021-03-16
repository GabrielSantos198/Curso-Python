print('\033[34m=\033[m'*35)
print('\033[1;35mMERCADINHO LOWRANSE\033[m'.center(45))
print('\033[34m=\033[m'*35)

preco = float(input('Qual o preço das compras? R$'))
print("""
\033[1;33mFORMAS DE PAGAMENTOS\033[m
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão
""")
opcao = int(input('Opção: '))
if opcao == 1:
    print('\033[1;32mNa Primeira opção de pagamento você teve um desconto de 10% na compra. De R${:.2f} ficou por R${:.2f}\033[m'.format(preco, preco-(preco*10/100)))
elif opcao == 2:
    print('\033[1;32mNa Segunda opção de pagamento você teve um desconto de 5% na compra. De R${:.2f} ficou por R${:.2f}\033[m'.format(preco, preco-(preco*5/100)))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} sem Juros'.format(preco/2))
elif opcao == 4:
    vezes = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} com Juros'.format(vezes, (preco+(preco*20/100))/vezes))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, preco+(preco*20/100)))
else:
    print('\033[1;31mEssa opção de pagamento não existe\033[m')

