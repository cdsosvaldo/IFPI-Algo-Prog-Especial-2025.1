def main():

    print(">>>>Sistema de Notas Escolares<<<<")

    nota1 = nota_entrada(1)
    nota2 = nota_entrada(2)
    nota3 = nota_entrada(3)

    notas = [nota1, nota2, nota3]

    media = calculo_media(notas)

    status = parametro_notas(media, notas)

    print(f"•Notas: {nota1:.1f} | {nota2:.1f} | {nota3:.1f}")
    print(f"•Média: {media:.2f}")
    print(f"•Situação do aluno: {status}")
    
def nota_entrada(valor: int) -> float:

    while True:
        try:       
            numero = float(input(f"Informe a nota {valor}: "))
            if 0.0 <= numero <= 10.0:
                return numero
            else:
                print("Inválido! Informe um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Informe um número para a nota.")

def calculo_media(notas: list[float]) -> float:

    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def parametro_notas(media: float, notas: list[float]) -> str:

    if 0.0 in notas:
        return "Reprovado! - Você possui uma ou mais notas igual a 0"
    elif media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media <= 6.9:
        return "Recuperação"
    else: 
        return "Reprovado"


main()