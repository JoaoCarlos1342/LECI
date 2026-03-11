def inputFloatList():
    lst = []
    n = input("Enter a number: ")
    while n != "":
        lst.append(float(n))
        n = input("Enter a number: ")
    return lst

def countLower(lst,v):
    count = 0
    for i in lst:
        if i < v:
            count += 1
    return count

def minmax(lst):
    minimo = lst[0]
    maximo = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < minimo:
            minimo = lst[i]
        if lst[i] > maximo:
            maximo = lst[i]
    return minimo, maximo

def main():
    lista = inputFloatList()
    print("Esta é a lista")
    print(lista)
    mini, maxi = minmax(lista)
    print("O valor mínimo da lista é {} e o valor máximo da lista é {}".format(mini, maxi))
    media = (mini + maxi)/2
    print("Média entre o máximo e o mínimo é {}".format(media))
    print("Há {} números com o valor inferior ao valor da média entre o mínimo e o máximo". format(countLower(lista, media)))
    return 0

main()