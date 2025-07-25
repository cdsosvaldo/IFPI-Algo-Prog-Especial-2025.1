from utils import obter_inteiro_positivo

def main():

    print(">>>>Verificador de Números Primos<<<<")
    numero = obter_inteiro_positivo("Informe um número inteiro positivo: ")

    if eh_primo(numero):
        print(f"'{numero}' é um número primo!")
    else:
        print(f"'{numero}' não é um número primo.")


def eh_primo(number: int) -> bool:

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


main()