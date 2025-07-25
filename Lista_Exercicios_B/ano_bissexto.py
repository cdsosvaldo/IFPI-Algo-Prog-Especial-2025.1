def main():

    ano_conversor = int(input("Informe um ano para verificar se é bissexto: "))

    if ano_bissexto(ano_conversor):
        print(f"'{ano_conversor}' é um ano bissexto.")
    else:
        print(f"'{ano_conversor}' não é um ano bissexto.")

def ano_bissexto(ano: int) -> bool:
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

main()