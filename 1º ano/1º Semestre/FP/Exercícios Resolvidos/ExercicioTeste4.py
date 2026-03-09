# Programa para gerar o Triângulo de Pascal

# Pedimos ao utilizador o número de linhas
n = int(input("Número de linhas do Triângulo de Pascal: "))

# Lista que vai guardar todas as linhas do triângulo
triangulo = []

# Loop para criar cada linha do triângulo
for i in range(n):
    # Cada linha começa como uma lista vazia
    linha = []

    # Loop para preencher os elementos da linha
    for j in range(i + 1):
        # O primeiro e o último elemento de cada linha são sempre 1
        if j == 0 or j == i:
            linha.append(1)
        else:
            # Elementos internos são a soma dos dois elementos acima
            linha.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])

    # Adicionamos a linha completa ao triângulo
    triangulo.append(linha)

# Impressão do triângulo linha por linha
for linha in triangulo:
    print(linha)

#Não acho que vás conseguir fazer este por ti mesma mas acho que consegues entender o que está aqui escrito