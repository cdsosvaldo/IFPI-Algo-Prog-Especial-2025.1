def main():

    num = int(input("Quantos números deseja informar? "))

    soma = 0.0

    print(f"Agora digite os {num} números:")

    for i in range(1, num + 1):
        numero = float(input(f"Digite o {i}º número: "))
        soma = soma + numero

    media = soma / num

    print(f"•Soma dos números: {soma:.2f}")
    print(f"•Média dos números: {media:.2f}")

main()