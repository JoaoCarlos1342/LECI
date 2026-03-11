def main():
    lst = []
    contador = 0
    soma = 0
    num = int(input("Qual é o número? "))
    
    for i in range(1, num):
        if num % i == 0:
            contador += 1
            soma += i
            lst.append(i)
        
    print("Os divisores do número {} são {}".format(num, lst))
    if soma < num:
        print("Deficiente")

    elif soma == num:
        print("Perfeito")

    else:
        print("Abundante")

main()