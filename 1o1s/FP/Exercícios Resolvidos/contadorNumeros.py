def countDigits(string):
    contador = 0
    for char in string:
        if char.isdigit():
            contador += 1
    #resultado = print("Há {} números na string {}".format(contador, string))

    return contador

def main():
    string = input("Escreve números e palavras ")

    print(countDigits(string))

main()