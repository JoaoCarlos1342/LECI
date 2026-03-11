"""
Docstring for shorten
def shorten(string):
    lista = []
    for char in string:
        if char.isupper():
            lista.append(char)

    return "".join(lista)
"""

def shorten(string):
    resultado = "" 
    
    for char in string:
        if char.isupper():
            resultado = resultado + char

    return resultado

def main():
    string = input("Escree algo que só vão fiar as letras maiúsculas: ")
    
    print(shorten(string))

main()