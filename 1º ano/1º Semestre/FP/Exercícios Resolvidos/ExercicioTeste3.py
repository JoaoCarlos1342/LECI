def main():
    # Inputs
    pas = int(input("Pressão arterial sistólica (mmHg): "))
    col = int(input("Colesterol total (mg/dL): "))
    fumador = input("Fumador (s/N/S/n): ")
    #Não comeces a panicar isto é uma matriz e tu já sabes fazer isso
    # Tabela de risco para NÃO fumadores
    tabela_nf = [
        [0, 0, 1, 1, 1],   # até 120
        [0, 1, 1, 1, 1],   # até 140
        [1, 1, 1, 1, 1],   # até 160
        [1, 1, 1, 1, 1]    # acima de 160
    ]
    # Tabela de risco para FUMADORES
    tabela_f = [
        [0, 1, 1, 2, 2],
        [1, 1, 1, 1, 2],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    # Determinar linha pela pressão arterial
    if pas <= 120:
        lin = 0
    elif pas <= 140:
        lin = 1
    elif pas <= 160:
        lin = 2
    else:
        lin = 3
    # Determinar coluna pelo colesterol
    if col <= 150:
        col_idx = 0
    elif col <= 200:
        col_idx = 1
    elif col <= 250:
        col_idx = 2
    elif col <= 300:
        col_idx = 3
    else:
        col_idx = 4
    # Escolher tabela dependendo se é fumador
    if fumador.lower() == "s":
        risco = tabela_f[lin][col_idx]
    else:
        risco = tabela_nf[lin][col_idx]
    # Output final
    print("O risco cardiovascular =", risco)
main()