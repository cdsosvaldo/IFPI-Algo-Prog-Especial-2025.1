def main():
        
        numero = int(input("Digite um número: "))

        total_digitos = contador_dgts(numero)

        if total_digitos is not None:
            print(f"O número informado tem {total_digitos} dígito(s).")
        else:
            return
            
def contador_dgts(numero):

    num_abs = abs(numero)

    if num_abs == 0:
        return 1

    contador_digitos = 0

    while num_abs > 0:
        num_abs = num_abs // 10
        contador_digitos = contador_digitos + 1 
    return contador_digitos



main()