def media(lst):
    soma = 0
    for i in range(len(lst)):
            soma += lst[i]

    media = soma/len(lst)

    return media

def main():
    lst = []
    num = 0
    while True:
        num = input("Adiciona um número ")
        if num != "":
            num = int(num)
            lst.append(num)

        else:
            break
    
    print("A média da tua lista {} é {}".format(lst, media(lst)))

main()