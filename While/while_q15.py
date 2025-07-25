def main():

        num_decimal = int(input("Informe um número entre 0 e 255: "))

        print(f"•Número Decimal: {num_decimal}")

        num_binario = num_decimal
        binario = ""

        if num_binario == 0:
            binario = "0"
        else:
            while num_binario > 0:
                resto = num_binario % 2
                binario = str(resto) + binario
                num_binario = num_binario // 2
        
        print(f"•Número Binário: {binario}")
        
        num_hexa = num_decimal
        hexadecimal = ""
        
        digitos_hex = "0123456789ABCDEF"

        if num_hexa == 0:
            hexadecimal = "0"
        else:
            while num_hexa > 0:
                resto = num_hexa % 16
                hexadecimal = digitos_hex[resto] + hexadecimal
                num_hexa = num_hexa // 16

        print(f"•Número Hexadecimal: {hexadecimal}")

main()