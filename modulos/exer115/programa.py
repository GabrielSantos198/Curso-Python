import dados

cores = {'padrao':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m'}

while True:
    dados.titulo('MENU PRINCIPAL')
    print(f"""
{cores['amarelo']}1{cores['padrao']} - {cores['azul']}Ver pessoas cadastradas
{cores['amarelo']}2{cores['padrao']} - {cores['azul']}Cadastrar nova Pessoa
{cores['amarelo']}3{cores['padrao']} - {cores['azul']}Sair do Sistema{cores['padrao']}
""",end='')
    print('-'*40)
    try:
        opcao = int(input('\033[33mSua Opção: \033[m'))
    except KeyboardInterrupt:
        print('\033[1;31mO usuário decidiu não informar nem um valor.\033[m')
        break
    except:
        print('\033[1;31mErro: Por favor digite um número de tipo válido\033[m')
    else:
        if opcao == 1:
            dados.cadastros()
        elif opcao == 2:
            dados.novo()
        elif opcao == 3:
            break
        else:
            print('\033[1;31mOpção Inexistente... Por favor digite Novamente\033[m')
print('\033[1;44;35m<<< Fim do Programa >>>\033[m')

