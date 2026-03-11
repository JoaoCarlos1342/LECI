# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:30s} : {:30s}".format("Numero", "Nome", "Morada"))
    for num, (nome, morada) in dic.items():
        print("{:>12s} : {:^30s} : {:<30s}".format(num, nome, morada))

def filterPartName(contacts, partName):
    matches = {}
    for num, dados in contacts.items():
        nome, morada = dados
        if partName.lower() in nome.lower():
            matches[num] = dados
    return matches

def addContact(dic):
    num = input("Qual número deseja adicionar? ")
    if num in dic:
        print("Esse número já existe.")
        return
    
    nome = input("Qual é o nome? ")
    morada = input("Qual é a morada? ")
    dic[num] = (nome, morada)
    print("Contacto adicionado.")

def searchContact(dic):
    num = input("Qual contacto desejas procurar? ")
    dados = dic.get(num)

    if dic.get(num) == None:
        return print(num)
    else:
        nome, morada = dados
        print("Nome: {}".format(nome))
        print("Morada: {}".format(morada))
    
def removeContact(dic):
    num = input("Que contacto deseja remover? ")
    if num in dic:
        dic.pop(num)
        print("Contacto eliminado")
    else:
        print("Contacto não existe.")

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op




def mainloop(contactos):
    """Repeatedly show menu and execute user actions on given dictionary."""

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
        elif op == "R":
            removeContact(contactos)
        elif op == "N":
            searchContact(contactos)
        elif op == "P":
            pesquisa = input("Parte do nome? ")
            resultados = filterPartName(contactos, pesquisa)
            listContacts(resultados)
        else:
            print("Não implementado!")


def main():
    """Start the program."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro", "Madeira"),
        "387719992": ("Maria Matos", "Porto"),
        "887555987": ("Marta Maia", "Coimbra"),
        "876111333": ("Carlos Martins", "Porto"),
        "433162999": ("Ana Bacalhau", "Lisboa")
        }

    # Enter loop to interact with the user
    mainloop(contactos)


# O programa começa aqui
if __name__ == "__main__":
    main()

"""
dicionario = {}
tuplo = ()
lista = []
"""