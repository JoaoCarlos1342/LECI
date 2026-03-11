
ALTURA = 3.0  # Altura em metros de um andar
VIAGENS = 4   # Número de viagens diárias feitas por cada morador

def distanciaElevador(predio):
    for i in range(1, len(predio)):
        metros = predio[i] * i * ALTURA * VIAGENS

    return metros

def main():
    # Numero de moradores em cada piso de um prédio:
    #predio = [4, 2, 3, 8, 3]  # 4 moradores no piso 0, 2 no piso 1, ...
    predio = []
    i = 0
    while True:
        num = input("Quantos moradores tem no piso {}? ".format(i))
        if num == "":
            break
        else:
            num = int(num)
            predio.append(num)
            i += 1
    # Calcular distância percorrida pelo elevador num dia
    m_por_dia = distanciaElevador(predio)

    # E a distância percorrida num ano
    km_por_ano = m_por_dia * 10**-3 * 365

    # Mostrar resultado
    print("No predio", predio)
    print("o elevador percorre", m_por_dia, "m por dia")
    print("ou seja, {:.2f} km por ano".format(km_por_ano)) 



if __name__ == "__main__":
    main()

