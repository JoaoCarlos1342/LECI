# Complete o programa!

# a)

# coluna 0 é Número
# coluna 1 é Nome
# coluna 5 é nota1
# coluna 6 é nota2
# coluna 7 é nota3

def loadFile(fname, lst):
    with open(fname, "r", encoding="utf-8") as fin:
        fin.readline()
        for line in fin:
            linha = line.strip().split("\t")
            lst.append((int(linha[0]), linha[1], float(linha[5]), float(linha[6]), float(linha[7])))

    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    return (reg[2] + reg[3] + reg[4]) / 3

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print(f"{'Numero':>8} {'Nome':^45} {'Nota':>6}")
    print("-" * 61)
    
    for reg in lst:
        # Chama a função e formata diretamente dentro do print
        print(f"{reg[0]:>8} {reg[1]:^45} {notaFinal(reg):>6.1f}")

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


