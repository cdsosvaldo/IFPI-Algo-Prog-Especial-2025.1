def main():

    horas_prof1 = float(input("Professor 1 - Informe a quantidade de horas/aula: "))
    valor_hora_prof1 = float(input("Professor 1 - Informe o valor por hora (R$): "))
    horas_prof2 = float(input("Professor 2 - Informe a quantidade de horas/aula: "))
    valor_hora_prof2 = float(input("Professor 2 - Informe o valor por hora (R$): "))

    salario_prof1 = horas_prof1 * valor_hora_prof1
    salario_prof2 = horas_prof2 * valor_hora_prof2

    print(f"Professor 1 - Salário: R$ {salario_prof1:.2f}")
    print(f"Professor 2 - Salário: R$ {salario_prof2:.2f}")

    if salario_prof1 > salario_prof2:
        print("•O Professor 1 tem o salário total maior.")  
    else:
        print("•O Professor 2 tem o salário total maior.")
 

main()