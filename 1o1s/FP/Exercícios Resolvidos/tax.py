def tax(r):
    if r <= 1000:
        taxa = 0.1 * r
    elif 1000 < r <= 2000:
        taxa = 0.2 * r - 100
    else:
        taxa = 0.3 * r - 300
    return taxa

def main():
    r = float(input("Qual é o r? "))

    print("Para r = {} a taxa é {}".format(r, tax(r)))

main()