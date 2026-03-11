"""
Docstring for compareFiles
def compareFiles(fname):
    f = open(fname, "rb")
    conteudo = f.read()
    f.close()
    return conteudo

def main():
    ficheiro1 = compareFiles("pg3333.txt")
    ficheiro2 = compareFiles("pg3336.txt")
    print(ficheiro1)
    print(ficheiro2)

    if ficheiro1 == ficheiro2:
        print("Os dois ficheiros são iguais")
    else:
        print("Os dois fichiero não são iguais")
main()
"""


import sys

def compareFiles(fname1, fname2):
    # Tamanho do bloco: 1 KiB = 1024 bytes
    BLOCK_SIZE = 1024
    
    try:
        # Abrir simultaneamente dois ficheiros na mesma instrução 'with'
        with open(fname1, "rb") as f1, open(fname2, "rb") as f2:
            while True:
                # Ler um bloco de cada ficheiro
                bloco1 = f1.read(BLOCK_SIZE)
                bloco2 = f2.read(BLOCK_SIZE)
                
                # Se os blocos forem diferentes, os ficheiros são diferentes
                if bloco1 != bloco2:
                    return False
                
                # Se um dos blocos estiver vazio (b''), chegámos ao fim do ficheiro.
                # Como eles são iguais até aqui (passaram no if acima), 
                # se um acabou, o outro também tem de ter acabado para serem iguais.
                if not bloco1: 
                    return True
                    
    except FileNotFoundError:
        print("Erro: Um dos ficheiros não foi encontrado.")
        return False

def main():
    # --- ZONA DE CONFIGURAÇÃO ---
    # Escreve aqui o nome dos teus ficheiros entre aspas
    nome_ficheiro_1 = "pg3337.txt"
    nome_ficheiro_2 = "pg3336.txt"
    # ----------------------------

    print(f"A comparar '{nome_ficheiro_1}' com '{nome_ficheiro_2}'...")

    if compareFiles(nome_ficheiro_1, nome_ficheiro_2):
        print("RESULTADO: Os ficheiros são IGUAIS.")
    else:
        print("RESULTADO: Os ficheiros são DIFERENTES.")

if __name__ == "__main__":
    main()

"""
VERSÃO MAIS SIMPLES
import os  # Necessário apenas se quisermos verificar se o ficheiro existe sem usar try

def compareFiles(fname1, fname2):
    # Verificação de segurança (opcional, já que não podemos usar try)
    if not os.path.exists(fname1) or not os.path.exists(fname2):
        print("Erro: Um dos ficheiros não existe.")
        return False

    f1 = open(fname1, "rb")
    f2 = open(fname2, "rb")
    
    block_size = 1024
    
    while True:
        bloco1 = f1.read(block_size)
        bloco2 = f2.read(block_size)
        
        if bloco1 != bloco2:
            # IMPORTANTE: Fechar antes de sair
            f1.close()
            f2.close()
            return False
        
        if not bloco1: # Se o bloco estiver vazio, acabou
            # IMPORTANTE: Fechar antes de sair
            f1.close()
            f2.close()
            return True

def main():
    nome1 = input("Introduza o nome do primeiro ficheiro: ")
    nome2 = input("Introduza o nome do segundo ficheiro: ")
    
    resultado = compareFiles(nome1, nome2)
    
    if resultado:
        print("Os ficheiros são IGUAIS.")
    else:
        print("Os ficheiros são DIFERENTES.")

if __name__ == "__main__":
    main()
"""