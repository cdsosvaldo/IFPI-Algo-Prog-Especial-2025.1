def main():

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))


    if num1 > num2:
        print(f"{num1} é o maior número")
        print(f"{num2} é o menor número")
    elif num2 > num1:
        print(f"{num2} é o maior número")
        print(f"{num1} é o menor número")
    else:
        print("Os dois números são iguais.")


main()