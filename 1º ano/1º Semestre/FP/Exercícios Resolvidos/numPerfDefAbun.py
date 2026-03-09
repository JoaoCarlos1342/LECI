def divNum(number):
    counter = 0
    lista = []
    for i in range(1, number):
        if number%i == 0:
            counter += i
            lista.append(i)
    print(lista)
    if counter < number:
        print("O número é deficiente")
    elif counter == number:
        print("O número é perfeito")
    else:
        print("O número é abundante")
    return 0

def main():
    number = int(input("Digite um número: "))
    divNum(number)

main()