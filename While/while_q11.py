def main():

    alunos = 0
    aprovados = 0
    reprovados = 0

    while True:
        print(">Aluno")
        matricula = int(input("Digite a matrícula (0 para finalizar): "))

        if matricula == 0:
            print("Planilha finalizada!")
            break

        alunos = alunos + 1

        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10) or not (0 <= nota3 <= 10):
            print("Atenção: Notas devem estar entre 0 e 10!")
            
        media = calc_media_final(nota1, nota2, nota3)

        print(f"Média Final do aluno {matricula}: {media:.2f}")

        if media >= 7.0:
            print("•Status: APROVADO")
            aprovados = aprovados + 1
        else:
            print("•Status: REPROVADO")
            reprovados = reprovados + 1

    print(f'''
            >>> QUADRO <<<
    •Total de alunos informados: {alunos}
    •Total de alunos aprovados: {aprovados}
    •Total de alunos reprovados: {reprovados}
    ''')

def calc_media_final(nota1, nota2, nota3):
    media_final = (2 * nota1 + 3 * nota2 + 5 * nota3) / 10
    return media_final


main()