def fatorial(num):
    resultado = 1
    if num == 0 or num == 1:
        return 1
    
    while num > 0:
        resultado = resultado * num
        num -= 1

    return resultado
    
def main():
    numero = int(input("Qual é o número? "))
    print(fatorial(numero))
main()