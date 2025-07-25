def main():

        numero_chave = int(input("Digite o número: "))

        print(f"Agora, continue digitando números. O programa vai parar quando você encontrar a chave.")

        numero_atual = None

        while numero_atual != numero_chave:
            numero_atual = float(input("Digite um número: "))

            if numero_atual == numero_chave:
                print(f"Chave '{numero_chave}' encontrada!")
                print(">>FIM<<")
            else:
                print("Não é o número procurado. Continue digitando...")


main()