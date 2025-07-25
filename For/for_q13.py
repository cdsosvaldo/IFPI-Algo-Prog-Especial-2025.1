def main():

    num = int(input("Quantos números deseja informar? "))

    print(f"Agora digite os {num} números:")

    maior_numero = int(input("Digite o 1º número: "))

    for i in range(2, num + 1):
        numero_atual = int(input(f"Digite o {i}º número: "))

        if numero_atual > maior_numero:
            maior_numero = numero_atual

    print(f"•{maior_numero} é o maior número da lista.")

main()