import sys

def main():

    if len(sys.argv) < 2:
        print("Erro: Por favor, indique o nome do ficheiro.")
        print("Exemplo de uso: python contadorLetras.py pg3336.txt")
        sys.exit(1)

    nome_ficheiro = sys.argv[1]
    frequencia = {}
    contador = 0
    f = open("pg3333.txt", "r", encoding="utf-8")
    texto = f.read()

    for char in texto:
        if char.isalpha():
            char_lower = char.lower()
            contador += 1

            if char_lower in frequencia:
                frequencia[char_lower] += 1
            else:
                frequencia[char_lower] = 1
    
    letras_ordenadas = sorted(frequencia.keys())

    print(f"Frequência de letras em '{nome_ficheiro}':\n")
    print(f"{'Letra':<10} | {'Ocorrências'}")
    print("-" * 25)

    for letra in letras_ordenadas:
        print(f"{letra:<10} | {frequencia[letra]}")

    print("Os Lusíadas têm {} letras".format(contador))

main()