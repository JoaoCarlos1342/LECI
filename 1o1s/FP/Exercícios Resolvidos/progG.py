def trade_items(prices, Q, item, P1, P2):
    # Verifica stock do vendedor
    if P1.get(item, 0) < Q:
        return "NO-ITEM"
    
    cost = prices[item] * Q
    
    # Verifica dinheiro do comprador
    if P2.get("coins", 0) < cost:
        return "NO-COINS"
    
    # Executa transação
    P1[item] -= Q
    P1["coins"] += cost
    
    P2["coins"] -= cost
    P2[item] = P2.get(item, 0) + Q
    
    return "SUCCESS"

def gaming_history(gaming):
    history = {}
    for player, games in gaming.items():
        for game, dates in games.items():
            # max() funciona em tuplos (Ano, Mes, Dia) corretamente
            last_date = max(dates)
            
            if game not in history:
                history[game] = {}
            
            history[game][player] = last_date
    return history

def main():
    print("--- TESTE A: Transação de Itens ---")
    prices = {"sword": 150, "potion": 50, "shield": 300}
    
    # Estado inicial
    player1 = {"sword": 2, "potion": 5, "coins": 500} # Vendedor
    player2 = {"shield": 1, "coins": 200}             # Comprador
    
    print(f"Inicio P1: {player1}")
    print(f"Inicio P2: {player2}")

    # Teste 1: P2 tenta comprar 1 sword (Custo 150). P2 tem 200. OK.
    print("\n1. P2 tenta comprar 1 'sword' de P1...")
    result = trade_items(prices, 1, "sword", player1, player2)
    print(f"Resultado: {result}")
    print(f"P1 (após): {player1}") # Esperado: sword: 1, coins: 650
    print(f"P2 (após): {player2}") # Esperado: coins: 50, sword: 1

    # Teste 2: P2 tenta comprar mais 1 sword. Custo 150. P2 tem 50. ERRO (NO-COINS).
    print("\n2. P2 tenta comprar outra 'sword'...")
    result = trade_items(prices, 1, "sword", player1, player2)
    print(f"Resultado: {result}") # Esperado: NO-COINS

    # Teste 3: P2 tenta comprar 10 potions. P1 só tem 5. ERRO (NO-ITEM).
    print("\n3. P2 tenta comprar 10 'potion'...")
    result = trade_items(prices, 10, "potion", player1, player2)
    print(f"Resultado: {result}") # Esperado: NO-ITEM

    print("\n" + "="*40 + "\n")

    print("--- TESTE B: Histórico de Jogos ---")
    gaming = {
        "maria": {
            "Minecraft": {(2024, 1, 12), (2024, 1, 10)},
            "Portal 2":  {(2024, 1, 11)}
        },
        "rui": {
            "Minecraft": {(2024, 1, 9), (2024, 1, 15)},
            "Hades":     {(2024, 1, 10)}
        }
    }

    history = gaming_history(gaming)
    
    # Impressão formatada para verificar o resultado
    for game, players in history.items():
        print(f"Jogo: {game}")
        for player, date in players.items():
            print(f"  - {player}: {date}")

if __name__ == "__main__":
    main()