from tkinter import filedialog

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    soma = 0.0
    # Usamos 'with' para o Python fechar o ficheiro automaticamente no fim
    with open(filename, "r") as fin:
        for line in fin:
            # strip() remove espaços/quebras de linha; float() converte para número
            line = line.strip()
            if line:  # Ignora linhas vazias
                soma += float(line)
    return soma

"""
def fileSum(filename):
    soma = 0.0
    fin = open(filename, "r")
    
    while True:
        line = fin.readline()
        
        # Se a linha for uma string vazia, atingimos o fim do ficheiro
        if line == "":
            break
            
        # Converter para float (strip remove o \n e espaços extras)
        dados = line.strip()
        if dados: # Verifica se a linha não está apenas em branco
            soma += float(dados)
            
    fin.close() # Aqui o fecho manual é obrigatório
    return soma
"""


if __name__ == "__main__":
    main()

