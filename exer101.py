def voto(nasc):
    from datetime import date

    idade = (date.today().year) - nasc
    if idade >= 18 and idade < 60:
        return f"Com {idade} anos: Voto é Obrigatório"
    elif idade < 18:
        return f"Com {idade} anos: Você Não Vota"
    else:
        return f"Com {idade} anos: Seu Voto é Opcional"


nasc = int(input('Qual o seu ano de nascimento? '))
print(voto(nasc))

