def main():

    populacao_a = 200000.0 
    taxa_cresci_a = 0.035

    populacao_b = 800000.0
    taxa_cresci_b = 0.0135

    anos = 0

    print(f"População da Cidade A: {int(populacao_a)} habitantes (Taxa: {taxa_cresci_a * 100:.2f}%)")
    print(f"População da Cidade B: {int(populacao_b)} habitantes (Taxa: {taxa_cresci_b * 100:.2f}%)")


    while populacao_a <= populacao_b:
        anos = anos + 1
        populacao_a = populacao_a + (populacao_a * taxa_cresci_a)
        populacao_b = populacao_b + (populacao_b * taxa_cresci_b)

    print(f'''
        **** Resultado ****
    •População da Cidade A no ano {anos}: {int(populacao_a):,} habitantes
    •População da Cidade B no ano {anos}: {int(populacao_b):,} habitantes
    •Para que a população da Cidade A ultrapasse a população da Cidade B serão necessários {anos} anos.

    ''')

main()