"""
!!! FUNÇÕES EXTRA !!!

def showTeams(equipas):
    if not equipas:
        print("Não há equipas registadas")
    
    for j in equipas:
        print(j)

def removeTeam(equipas):
    nome = input("Que equipa deseja eliminar? ")
    if nome in equipas:
        equipas.remove(nome)
        print("Equipa eliminada")
    else:
        print("Essa equipa não existe")

"""

def adicionarEquipas(equipas):
    while True:
        equipa = input("Que equipa deseja adicionar? ")
        if equipa == "": # Condição para quebrar o loop infinito
            break

        if equipa in equipas: # Verifica se já existe a equipa na lista
            print("Essa equipas já existe")
        else:
            equipas.append(equipa) # Adiciona a equipa a lista
            print(f"Equipa {equipa} adicionada") # Também se pode escrever print("Equipa {} adicionada".format(equipa))

def gerarJogos(equipas):
    jogos = []
    if len(equipas) < 2:
        print("Não há equipas suficientes")
        return
    else:
        for i in range(len(equipas)):
            for j in range(len(equipas)):
                if equipas[i] != equipas[j]:
                    jogos.append((equipas[i], equipas[j]))

    return jogos

def registarResultados(jogos):
    resultados = {}
    for casa, fora in jogos:
        print("Jogo: {} vs {}".format(casa, fora))

        golosCasa = int(input("Quantos golos marcou {}? ".format(casa)))
        golosFora = int(input("Quantos golos marcou {}? ".format(fora)))

        resultados[(casa, fora)] = (golosCasa, golosFora) # Como aparece no exempo [('FCP', 'SLB')] -> (3, 2)

    return resultados

def calcularTabela(equipas, resultado):
    tabela = {}
    for equipa in equipas:
        tabela[equipa] = [0, 0, 0, 0, 0, 0] # Ordem da lista ---> Vitórias, Empates, Derrotas, Golos Marcados, Golos Sofridos, Pontos

    for jogo, golos in resultado.items(): #.items() vai retornar duas coisas então ao usar duas variáveis vou repartir essa informação. jogo vai receber o tuplo com os nomes das equipas e golos vai receber o tuplo dos golos de cada equipa
        casa, fora = jogo # aqui a lógica é a mesma como jogo tem dois nomes uso casa e fora para repartir essa informação
        golosCasa, golosFora = golos # o mesmo acontece aqui golosCasa e golosFora vão repartir a informação do tuplo golos

    # Atualizar Golos Marcados (GM - índice 3) e Sofridos (GS - índice 4)
        tabela[casa][3] += golosCasa
        tabela[casa][4] += golosFora
        tabela[fora][3] += golosFora
        tabela[fora][4] += golosCasa

        # Atualizar Vitórias, Empates, Derrotas e Pontos
        if golosCasa > golosFora:
            # Vitória da casa
            tabela[casa][0] += 1  # Vitórias
            tabela[casa][5] += 3  # Pontos
            tabela[fora][2] += 1  # Derrotas (visitante)
        elif golosFora > golosCasa:
            # Vitória de fora
            tabela[fora][0] += 1  # Vitórias
            tabela[fora][5] += 3  # Pontos
            tabela[casa][2] += 1  # Derrotas (casa)
        else:
            # Empate
            tabela[casa][1] += 1  # Empates
            tabela[casa][5] += 1  # Pontos
            tabela[fora][1] += 1  # Empates
            tabela[fora][5] += 1  # Pontos

    return tabela

def imprimirTabela(tabela):
    print("\n--- Tabela Classificativa ---")
    
    # Cabeçalho da tabela
    # :<15 (15 espaços à esquerda) | :^3 (3 espaços ao centro)
    print(f"{'Equipa':<15} | {'V':^3} | {'E':^3} | {'D':^3} | {'GM':^3} | {'GS':^3} | {'Pts':^3}") # :<, ^, > direção do ajuste sendo esquerda, centro e direita respetivamente e o número é a quantidade de carateres/espaços
    print("-" * 55)

    # Linhas da tabela
    for equipa, dados in tabela.items():
        v, e, d, gm, gs, pts = dados # "Desempacotar" a lista de dados
        print(f"{equipa:<15} | {v:^3} | {e:^3} | {d:^3} | {gm:^3} | {gs:^3} | {pts:^3}")

def encontrarCampeao(tabela):
    campeao = ""
    max_pontos = -1
    max_diff_golos = -1000 # Começamos com um valor muito baixo
    
    for equipa, dados in tabela.items():
        # Vamos buscar os dados que interessam
        gm = dados[3]
        gs = dados[4]
        pts = dados[5]
        diff = gm - gs # Cálculo da diferença de golos
        
        # Critério 1: Mais pontos
        if pts > max_pontos:
            max_pontos = pts
            max_diff_golos = diff
            campeao = equipa
            
        # Critério 2: Mesmos pontos, mas melhor diferença de golos
        elif pts == max_pontos:
            if diff > max_diff_golos:
                max_diff_golos = diff
                campeao = equipa
                
    print(f"\n🏆 O CAMPEÃO É: {campeao} com {max_pontos} pontos! 🏆")

def menu():
    print()
    print("(L)istar equipas")
    print("(A)dicionar equipa")
    print("(R)emover equipa")
    print("(G)erar jogos")
    print("(I)nserir resultado e Ver Tabela")
    print("(T)erminar")
    op = input("opção? ").upper()   # converte a letra para maiúscula
    return op

def mainloop(equipas):
    jogos = []
    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Equipas:", equipas)
        elif op == "A":
            adicionarEquipas(equipas)
        elif op == "R":
            nome = input("Que equipa deseja remover? ")
            if nome in equipas:
                equipas.remove(nome)
                print("Equipa removida.")
            else:
                print("Equipa não encontrada.")
        elif op == "G":
            if len(equipas) < 2:
                print("Precisa de pelo menos 2 equipas para gerar jogos.")
            else:
                jogos = gerarJogos(equipas)
                print("Foram gerados {} jogos.".format(len(jogos)))
                print(jogos)
        elif op == "I":
            if not jogos:
                print("Não há jogos gerados! Use (G) primeiro.")
            else:
                resultados = registarResultados(jogos)
                tabela = calcularTabela(equipas, resultados)
                imprimirTabela(tabela)
                encontrarCampeao(tabela)
        else:
            print("Opção inválida!")

def main():
    equipas = []
    mainloop(equipas)

if __name__ == "__main__":
    main()