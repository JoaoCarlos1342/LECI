def max2(n1, n2):
    if n1 > n2:
        maximo2 = n1
    else:
        maximo2 = n2
    return maximo2

def max3(n1, n2, n3):
    maximo = max2(max2(n1,n2),n3)
    return maximo

def main():
    n1 = int(input("Qual é o primeiro número? "))
    n2 = int(input("Qual é o segundo número? "))

    print("O maior número é", max2(n1, n2))

    n3 = int(input("Qual é o terceiro número? "))

    print("O maior número é", max3(n1, n2, n3))

main()