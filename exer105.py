def notas(*n,sit=False):
    """
    *n: Empacota uma quantidade ilimitada de números.
    sit: Recebe o valor True ou False. Esse parâmetro serve pra mostrar ou não a situação da sala.
    A função joga todos os dados dentro de um dicionario e retorna tudo no final.
    Autor: GabrielSantos198
    Obrigado por usar meu código!
    """

    dic = {}
    dic['quantidade'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    media = str(f'{sum(n) / len(n):.2f}')
    dic['media'] = float(media)
    if sit == True:
        if dic['media'] >= 7:
            dic['situacao'] = str('Boa')
        elif dic['media'] < 7 and dic['media'] >= 5:
            dic['situacao'] = str('Razoável')
        else:
            dic['situacao'] = str('Ruim')
    return dic


res = notas(5.5,2.5,1.5,sit=True)
print(res)
