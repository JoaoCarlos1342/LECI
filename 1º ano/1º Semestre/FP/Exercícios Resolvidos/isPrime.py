def isPrime(n):
    print(n)
    for i in range(1, n):
        if n%i == 0:
            return True
        else:
            return False

def main():
    number = int(input("Digite um número: "))
    if isPrime(number) == True or number == 1:
        print("O número é primo")
    else:
        print("O número não é primo")
    return 0

main()