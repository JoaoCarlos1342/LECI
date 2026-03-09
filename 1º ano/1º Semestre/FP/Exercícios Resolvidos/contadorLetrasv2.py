def contadorLetrasv2(fname):
    frequencia = {}    
    try:
        with open(fname, "r", encoding="utf-8") as f:
            texto = f.read()

            for char in texto:
                if char.isalpha():
                    char_lower = char.lower()

                    if char_lower in frequencia:
                        frequencia[char_lower] += 1
                    
                    else:
                        frequencia[char_lower] = 1
    

    except:
        FileNotFoundError("ESSE FICHEIRO NÃO EXISTE")

    letras_ordenadas = sorted(frequencia.items(), key=lambda x:x[1], reverse=True)

    print(f"Frequência de letras em '{fname}':\n")
    print(f"{'Letra':<10} | {'Ocorrências'}")
    print("-" * 25)

    for letra, contagem in letras_ordenadas:
        print(f"{letra:<10} | {contagem}")

def main():
    fname = input("Qual o nome do ficheiro? ")

    contadorLetrasv2(fname)

main()