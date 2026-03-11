import matches

def showTeams(equipas):
    if not equipas:
        print("Não há equipas registadas")
    
    for j in equipas:
        print(j)

def addTeam(equipas):
    nome = input("Que equipa deseja adicionar? ")

    if nome in equipas:
        print("Essa equipas já existe")
    else:
        equipas.append(nome)
        print(f"Equipa {nome} adicionada")
        
def removeTeam(equipas):
    nome = input("Que equipa deseja eliminar? ")
    if nome in equipas:
        equipas.remove(nome)
        print("Equipa eliminada")
    else:
        print("Essa equipa não existe")

def printTable(tabela):
    print("\n {:^15s} | {:^3s} | {:^3s} | {:^3s} | {:^3s} | {:^3s} | {:^3s}".format("Equipa", "V", "E", "D", "GM", "Pts"))
    print("-" * 60)
    
    for equipa, dados in tabela.items():
        v, e, d, gm, gs, pts = dados
        print("\n {:^15s} | {:^3s} | {:^3s} | {:^3s} | {:^3s} | {:^3s} | {:^3s}".format(equipa, v, e, d, gm, pts))
        print("-" * 60)

def findChampion(tabela):
    melhor_equipa = ""
    max_pontos = -1
    max_diff_golos = -1000

    for equipa, dados, in tabela.items():
        pontos = dados[5]
        diff_golos = dados[3] - dados[4]

        if pontos > max_pontos:
            max_pontos = pontos
            max_diff_golos = diff_golos
            melhor_equipa = equipa
        elif pontos == max_pontos:
            if diff_golos > max_diff_golos:
                max_diff_golos = diff_golos
                melhor_equipa = equipa
    return melhor_equipa, max_pontos

def runChampionship(equipas, jogos):
    if not jogos:
        print("Não há jogos gerados! Use (G) primeiro.")
        return
    
    tabela = {}
    for eq in equipas:
        tabela[eq] = [0, 0, 0, 0, 0, 0]

    print("\n--- Início do Campeonato ({}) jogos ---".format(len(jogos)))

    for casa, fora in jogos:
        print("\nJogo: {} vs {}".format(casa, fora))
        try:
            g_casa = int(input("Golo de {}".format(casa)))
            g_fora = int(input("Golo de {}".format(fora)))
        except:
            print("Valor inválido! Vamos assumir 0-0.")
            g_casa, g_fora = 0, 0

        tabela[casa][3] += g_casa
        tabela[casa][4] += g_fora
        tabela[fora][3] += g_fora
        tabela[fora][4] += g_casa

        if g_casa > g_fora:
            tabela[casa][0] += 1
            tabela[casa][5] += 3
            tabela[fora][2] += 1
        elif g_fora > g_casa:
            tabela[fora][0] += 1
            tabela[fora][5] += 3
            tabela[casa][2] += 1
        else:
            tabela[casa][1] += 1
            tabela[casa][5] += 1
            tabela[fora][1] += 1
            tabela[fora][5] += 1
        
    printTable(tabela)

    campeao, pontos = findChampion(tabela)
    print("\nO CAMPEÃO É: {} com {} pontos!".format(campeao, pontos))

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar equipas")
    print("(A)dicionar equipa")
    print("(R)emover equipa")
    print("(G)erar jogos")
    print("(I)nserir resultado")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def mainloop(equipas):
    """Repeatedly show menu and execute user actions on given dictionary."""
    jogos = []
    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Equipas:")
            showTeams(equipas)
        elif op == "A":
            addTeam(equipas)
        elif op == "R":
            removeTeam(equipas)
        elif op == "G":
            if len(equipas) < 2:
                print("Precisa de pelo menos 2 equipas para gerar jogos.")

            else:
                jogos = matches.allMatches(equipas)
                print("Foram gerados {} jogos.".format(len(jogos)))
                print(jogos)
        elif op == "I":
            runChampionship(equipas, jogos)
        else:
            print("Não implementado!")

def main():
    equipas = []
    mainloop(equipas)

main()