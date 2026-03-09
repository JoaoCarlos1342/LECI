def rec_soma(lst):
    soma = 0

    for item in lst:
        if isinstance(item, int):
            soma += item
        elif isinstance(item, list):
            soma += rec_soma(item)
    return soma

def main():
    lista_teste = ['one', 2, ['three', 4, [5, 'six']], 'ten']
    resultado = rec_soma(lista_teste)
    
    print(f"Lista: {lista_teste}")
    print(f"Soma esperada: 11")
    print(f"Soma obtida: {resultado}")

    lista_extra = [1, [2, [3, [4, 'texto']]], [], 10]
    print(f"\nLista extra:{lista_extra}")
    print(f"Soma obtida: {rec_soma(lista_extra)}")

if __name__ == "__main__":
    main()