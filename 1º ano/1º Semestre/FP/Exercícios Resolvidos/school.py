"""
# Complete o programa!

# a)
def loadFile(fname, lst):
    ...
    
# b) Crie a função notaFinal aqui...
...

# c) Crie a função printPauta aqui...
...

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()
"""
# Complete o programa!

# a)
# Complete o programa!

# a)
def loadFile(fname, lst):
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            f.readline() # Saltar cabeçalho
            for line in f:
                p = line.strip().split('\t')
                if len(p) >= 8: # Garante que a linha tem colunas suficientes
                    try:
                        # Adiciona diretamente: indices 0 (num), 1 (nome), 5,6,7 (notas)
                        lst.append((int(p[0]), p[1], float(p[5]), float(p[6]), float(p[7])))
                    except ValueError:
                        pass # Ignora linhas com erros de dados sem chatear
    except FileNotFoundError:
        print(f"Erro: {fname} não encontrado.")

# b)
def notaFinal(reg):
    # reg[2], reg[3], reg[4] são as notas dentro do tuplo criado acima
    return (reg[2] + reg[3] + reg[4]) / 3

# c)
def printPauta(lst):
    print(f"{'Numero':>8} {'Nome':^45} {'Nota':>6}")
    print("-" * 46)
    
    for reg in lst:
        # Chama a função e formata diretamente dentro do print
        print(f"{reg[0]:>8} {reg[1]:^45} {notaFinal(reg):>6.1f}")

# d)
def main():
    lst = []
    
    # Carregar ficheiros de 1 a 3 num loop simples
    for i in range(1, 4):
        loadFile(f"school{i}.csv", lst)
    
    lst.sort() # Ordena pelo número (primeiro elemento do tuplo)
    printPauta(lst)

if __name__ == "__main__":
    main()