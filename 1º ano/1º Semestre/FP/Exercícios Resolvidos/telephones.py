# Convert a telephone number into corresponding name, if on list.
# (If not on list, just return the number itself.)
def telToName(tel, telList, nameList):
    # Verifica se o número existe na lista
    if tel in telList:
        # Descobre a posição (índice) desse número
        index = telList.index(tel)
        # Retorna o nome que está na MESMA posição na outra lista
        return nameList[index]
    else:
        # Se não existir, retorna o próprio número
        return tel

# Return list of telephone numbers corresponding to names containing partName.
def nameToTels(partName, telList, nameList):
    tels = []
    # Percorre todos os nomes pelo índice
    for i in range(len(nameList)):
        # Verifica se o excerto (partName) está dentro do nome atual.
        # O uso de .lower() é excelente para ignorar maiúsculas/minúsculas
        if partName.lower() in nameList[i].lower():
            # Se encontrar, adiciona o número correspondente à lista de resultados
            tels.append(telList[i])
    return tels

def main():
    # Lists of telephone numbers and names
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    # Test telToName:
    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    
    # Testes automáticos (devem dar True)
    print("Teste Brad:", telToName('234000111', telList, nameList) == "Brad")
    print("Teste Desconhecido:", telToName('222333444', telList, nameList) == "222333444")

    print("-" * 20)

    # Test nameToTels:
    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    
    # Testes automáticos (devem dar True)
    print("Teste Clau:", nameToTels('Clau', telList, nameList) == ['777888333'])
    print("Teste Br:", nameToTels('Br', telList, nameList) == ['234000111', '911911911'])

if __name__ == "__main__":
    main()