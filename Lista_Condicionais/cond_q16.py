def main():

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    media_inicial = (nota1 + nota2) / 2.0

    if media_inicial >= 7.0:
        print(f"•Média: {media_inicial:.1f}")
        print("•Situação: >>APROVADO<<")
    else:
        print(f"•Média: {media_inicial:.1f}")
        print("•Situação: Necessário fazer exame.")

        nota_exame = float(input("Nota do Exame: "))

        media_final = (media_inicial + nota_exame) / 2.0

        print(f"•Média do Exame: {nota_exame:.1f}")
        print(f"•Média Final: {media_final:.1f}")

        if media_final >= 5.0:
            print("•Situação: >>APROVADO<<")
        else:
            print("•Situação: >>REPROVADO<<")


main()