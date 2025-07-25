def main():

    dividendo = int(input("Informe o valor (dividendo): "))
    divisor = int(input("Informe o valor (divisor): "))

    if divisor == 0:
        print("Inválido! Não é possível dividir por zero!")
        return
        
    dividendo_abs = abs(dividendo)
    divisor_abs = abs(divisor)

    quoci_abs = 0
    resto_abs = dividendo_abs

    while resto_abs >= divisor_abs:
        resto_abs = resto_abs - divisor_abs
        quoci_abs = quoci_abs + 1
        
    if dividendo < 0 and resto_abs != 0:
        resto_final = -resto_abs
    else:
        resto_final = resto_abs

    print(f'''
••••••••••••••••••••••••
          
•Dividendo: {dividendo}
•Divisor: {divisor}
•Resto: {resto_final}
''')

main()