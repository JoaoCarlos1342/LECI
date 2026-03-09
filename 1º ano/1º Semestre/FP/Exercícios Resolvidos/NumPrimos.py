def isPrime(num):
    contas = num//2
    for i in range(contas, 1, -1):
        if num%i == 0:
            return "Não é primo"
        
    return "É primo"

def main():
    num = int(input("Qual é o número? "))

    print(isPrime(num))

main()