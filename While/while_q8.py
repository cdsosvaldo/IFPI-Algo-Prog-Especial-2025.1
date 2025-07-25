def main():

    valor = int(input("Digite um número: "))
        
    referencia(valor)
        
def referencia(x_referencia):

    print("Agora digite os números um por um.")

    num_anterior = None
    num_atual = None

    print("•Lista - Digite o 1º número:")
    num_anterior = float(input("Número: "))
    print(f"Número registrado: {num_anterior}")

    print("•Lista - Digite o 2º número:")
    num_atual = float(input("Número: "))
    print(f"Número registrado: {num_atual}")

    while (num_anterior + num_atual) != x_referencia:
        print("Continue digitando números:")
        num_anterior = num_atual
            
        num_atual = float(input("Número: "))
        print(f"Número registrado: {num_atual}")

    print(f"> A soma de ({num_anterior} + {num_atual}) = {num_anterior + num_atual}.")
    print(">>Fim<<")



main()