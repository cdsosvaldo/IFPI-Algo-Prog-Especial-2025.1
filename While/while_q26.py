def main():
    print("•••• AVALIAÇÃO DO FILME ASSISTIDO ••••")
    print("Valores válidos: 1=ótimo, 2=bom, 3=regular, 4=péssimo")

    idades_otimo = 0
    total_otimo = 0
    total_regular = 0
    total_bom = 0
    entrevistados = 0

    idade = 0

    while idade != -1:

        idade = int(input("Digite a idade [-1 para finalizar]: "))

        if idade == -1:
            print("Pesquisa finalizada!")
            break
 
        if idade <= 0:
            print("Idade inválida!")
            continue

        opiniao = int(input("Digite a opinião (1=ótimo, 2=bom, 3=regular, 4=péssimo): "))

        if opiniao not in [1, 2, 3, 4]:
            print("Opção não registrada! Informe um valor válido.")
            continue

        entrevistados = entrevistados + 1

        if opiniao == 1:
            idades_otimo = idades_otimo + idade
            total_otimo = total_otimo + 1
        elif opiniao == 2:
            total_bom = total_bom + 1
        elif opiniao == 3:
            total_regular = total_regular + 1

    print("--- Apuração ---")

    if total_otimo > 0:
        media_otimo = idades_otimo / total_otimo
        print(f"•Média de idade dos que responderam 'ótimo': {media_otimo:.1f} anos")
    else:
        print("•Nenhuma pessoa respondeu 'ótimo'.")

    print(f"•Total de pessoas que respondeu 'regular': {total_regular}")

    if entrevistados > 0:
        percen_bom = (total_bom / entrevistados) * 100
        print(f"•Percentual de pessoas que respondeu 'bom': {percen_bom:.2f}%")
        print('>>>FIM<<<')

main()