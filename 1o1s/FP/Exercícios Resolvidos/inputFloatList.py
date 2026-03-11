def inputFloatList():
    lst = []
    while True:
        num = input("Insere um número na lista (clica ENTER para terminar)? ")
        if num == "":
            break
        else:
            num = int(num)
            lst.append(num)
    return lst

def countLower(lst, v):
    counter = 0
    for i in range(len(lst)):
        if lst[i] < v:
            counter += 1
    return counter

def minmax(lst):
    min = lst[0]
    max = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
    return min, max

def main():
    lst = inputFloatList()
    minimo, maximo = minmax(lst)
    print("A lista é {}".format(lst))
    v = (minimo + maximo) / 2
    print("Há {} números menores que {}".format(countLower(lst, v), v))
    print("O número mais pequeno é {} e o número maior é {}".format(minimo, maximo))

main()