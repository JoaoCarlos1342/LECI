#Exercicio 1 teste
participants = [('Ana', 13, 50, -1), ('Rita', 11, 15, 0), ('Pedro', 10, 40, 2), ('Tiago', 9, 50, 2),
                    ('Maria', 11, 25, 1)]
ultimo = participants[-1]

def pTime(pdata):
    minutos = participants[pdata][1]
    segundos = participants[pdata][2]
    penalizacao = participants[pdata][-1]
    total = minutos * 60 + segundos + penalizacao*60

    return total

def findTheBest(participants):
    for i in range(1, len(participants)):
        best = pTime(0)
        if pTime(i) < best:
            best = pTime(i)
        else:
            i += 1
    return best

def main():


    print("Participant at last index", ultimo)
    print("Total time for", ultimo[0], "is", pTime(4), "segundos" )
    print("The best participant is {}".format(findTheBest(participants)))

main()