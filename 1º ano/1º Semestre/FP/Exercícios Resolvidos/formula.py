def construir_molecula(lista_elementos):
    pedacos = []
    for simbolo, quantidade in lista_elementos:
        pedacos.append(simbolo)
        qtd_numero = int(quantidade)

        if qtd_numero > 1:
            pedacos.append(str(qtd_numero))
            print(qtd_numero)

    resultado = "".join(pedacos)
    return resultado

dados1 = [("H", 2), ("S", 1), ("O", 4)]
print(f"Lista: {dados1}")
print(f"Resultado: {construir_molecula(dados1)}")
print("-" * 20)

dados2 = [("Na", "1"), ("Cl", "1")]
print(f"Lista: {dados2}")
print(f"Resultado: {construir_molecula(dados2)}")