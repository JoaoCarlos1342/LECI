def mediana(lst):
    lista = sorted(lst)
    meio = len(lista)//2
    if len(lista)%2 == 0:
        mediana = (lista[meio-1] + lista[meio]) / 2
    else:
        mediana = lista[meio]
    
    return mediana

def main():
    lista = [2, 4, 5, 7, 9]
    lista2 = [5, 7, 8, 14, 16, 17]
    print(mediana(lista))
    print()
    print(mediana(lista2))

main()