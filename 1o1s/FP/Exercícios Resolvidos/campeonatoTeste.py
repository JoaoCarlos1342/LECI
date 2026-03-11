import random # Importante para gerar números aleatórios

# --- Funções Auxiliares ---
def allMatches(teams):
    matches = []
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                matches.append((team1, team2))
    return matches

def print_table(tabela):
    # Ordena a tabela por pontos (decrescente) para ficar mais realista
    # Lambda: ordena pelo índice 5 (pontos) e depois pelo 3 (GM)
    tabela_ordenada = sorted(tabela.items(), key=lambda x: (x[1][5], x[1][3]), reverse=True)

    print("\n{:^15} | {:^3} | {:^3} | {:^3} | {:^3} | {:^3} | {:^3}".format(
        "Equipa", "V", "E", "D", "GM", "GS", "Pts"))
    print("-" * 60)

    for equipa, dados in tabela_ordenada:
        v, e, d, gm, gs, pts = dados
        print("{:<15} | {:^3} | {:^3} | {:^3} | {:^3} | {:^3} | {:^3}".format(
            equipa, v, e, d, gm, gs, pts))
    print("-" * 60)
    
    return tabela_ordenada[0] # Retorna o primeiro (o campeão)

# --- Lógica de Simulação ---

def run_championship_auto(equipas, jogos):
    """
    Versão de TESTE: Gera resultados aleatórios em vez de pedir input.
    """
    if not jogos:
        print("Erro: Gere os jogos primeiro (Opção G).")
        return

    tabela = {}
    for eq in equipas:
        tabela[eq] = [0, 0, 0, 0, 0, 0] # [V, E, D, GM, GS, Pts]

    print(f"\n--- A SIMULAR {len(jogos)} JOGOS AUTOMATICAMENTE ---")
    
    for casa, fora in jogos:
        # GERAÇÃO ALEATÓRIA DE GOLOS (Entre 0 e 5)
        g_casa = random.randint(0, 5)
        g_fora = random.randint(0, 5)

        print("Jogo: {} {:>2} - {:<2} {}".format(casa, fora)) # Mostra o resultado gerado

        # Atualizar Tabela (Cópia da lógica anterior)
        tabela[casa][3] += g_casa
        tabela[casa][4] += g_fora
        tabela[fora][3] += g_fora
        tabela[fora][4] += g_casa

        if g_casa > g_fora:
            tabela[casa][0] += 1; tabela[casa][5] += 3; tabela[fora][2] += 1
        elif g_fora > g_casa:
            tabela[fora][0] += 1; tabela[fora][5] += 3; tabela[casa][2] += 1
        else:
            tabela[casa][1] += 1; tabela[casa][5] += 1
            tabela[fora][1] += 1; tabela[fora][5] += 1
            
    # Mostrar Tabela e Campeão
    campeao_dados = print_table(tabela)
    print(f"\n🏆 CAMPEÃO: {campeao_dados[0]} com {campeao_dados[1][5]} pontos! 🏆")

# --- Menus e Main ---

def menu():
    print("\n--- MENU DE TESTE ---")
    print("(L)istar equipas")
    print("(G)erar jogos")
    print("(S)imular Campeonato (TESTE RÁPIDO)") 
    print("(T)erminar")
    op = input("Opção? ").upper()
    return op

def main_teste():
    # 1. PRÉ-CARREGAR DADOS (Para não teres de adicionar equipas à mão)
    equipas = ["FCP", "SLB", "SCP", "Braga", "Vitoria SC"] 
    jogos = [] 

    print(">>> DADOS DE TESTE CARREGADOS <<<")
    print(f"Equipas iniciais: {equipas}")

    op = ""
    while op != "T":
        op = menu()
        
        if op == "T":
            print("Fim")
        elif op == "L":
            for eq in equipas: print(f"-> {eq}")
        elif op == "G":
            jogos = allMatches(equipas) 
            print(f"\nForam gerados {len(jogos)} jogos.")
        elif op == "S":
            # Aqui chamamos a função automática
            run_championship_auto(equipas, jogos)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main_teste()