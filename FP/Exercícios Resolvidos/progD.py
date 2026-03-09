# progD.py

def countPolluters(lst, M, E):
    """
    Conta modelos da marca M com emissões superiores a E.
    """
    count = 0
    for car in lst:
        marca = car[1]
        emissoes = car[3]
        if marca == M and emissoes > E:
            count += 1
    return count

def loadFile(filename, lst):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            f.readline()
            for line in f:
                line = line.strip()
                if not line: continue
                
                parts = line.split(':')
                if len(parts) == 5:
                    modelo = parts[0]
                    marca = parts[1]
                    cilindrada = int(parts[2])
                    emissoes = float(parts[3])
                    preco = float(parts[4])
                    
                    lst.append((modelo, marca, cilindrada, emissoes, preco))
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{filename}' não encontrado.")
    except ValueError:
        print("Erro: Problema na conversão de dados do ficheiro.")

def tableCars(lst):
    print("\nTABELA DE PREÇOS FINAIS")
    print(f"{'Marca':<10} {'Modelo':<10} {'Emissões':>10}   {'Eficiência':^10} {'PrecoFinal':>12}")
    print("-" * 60)

    for car in lst:
        modelo, marca, _, emissoes, preco = car
        
        if emissoes > 150:
            status = "DIRTY"
            final_price = preco * 1.05
        else:
            status = "ECO"
            final_price = preco * 0.90
            
        print(f"{marca:<10} {modelo:<10} {emissoes:>10.1f}   {status:^10} {final_price:>11.2f}€")

def main():
    cars = [
        ("Delta 1", "BMW", 2500, 114.5, 39957.4),
        ("Clio", "Renault", 1200, 110.0, 15000.0),
        ("M5", "BMW", 4400, 240.0, 120000.0)
    ]

    cars2 = [
        ("Alpha 2", "Audi", 2000, 190.0, 28904.18),
        ("Zeta 7", "BMW", 3000, 107.4, 43325.3),
        ("Golf", "VW", 2000, 130.0, 30000.0)
    ]

    print("--- ALÍNEA A: Teste countPolluters ---")
    # Deve devolver 1 (Apenas o BMW M5 tem emissões > 120 na lista cars original)
    res_a = countPolluters(cars, "BMW", 120) 
    print(f"BMWs com emissões > 120: {res_a}")

    print("\n--- ALÍNEA B: Teste loadFile ---")
    # Criar um ficheiro temporário para teste
    fname = "novos_carros.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write("Modelo:Marca:Cilindrada:Emissões:Preço\n") # Cabeçalho
        f.write("Yaris:Toyota:1000:99.5:18500.0\n")
        f.write("Mustang:Ford:5000:280.0:65000.0\n")
    
    loadFile(fname, cars)
    print(f"Tamanho da lista cars após carregar ficheiro: {len(cars)} (Esperado: 5)")
    print("Último carro adicionado:", cars[-1])

    print("\n--- ALÍNEA C: Teste tableCars ---")
    # Combina as listas para uma tabela maior
    todos_carros = cars + cars2
    tableCars(todos_carros)

    print("\n--- ALÍNEA D: SORT ---")
    cars2_sorted = sorted(cars2, key=lambda x: (-x[2], x[3]))
    
    print(f"{'Modelo':<10} {'Cilindrada':<10} {'Emissões':<10}")
    for c in cars2_sorted:
        print(f"{c[0]:<10} {c[2]:<10} {c[3]:<10}")

if __name__ == "__main__":
    main()