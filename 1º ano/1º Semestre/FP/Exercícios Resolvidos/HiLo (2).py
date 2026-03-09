import random

def main():
    tentativas = 0
    numero = random.randrange(1, 100)
    guess = int(input("Qual é o número que estou a pensar? "))
    while(True):
        
        if guess > numero:
            print("High")
            tentativas += 1
        
        elif guess < numero:
            print("Low")
            tentativas += 1

        else:
            print("Boa acertaste. Adivinhaste em {} tentativas".format(tentativas))
            break
        guess = int(input("Qual é o número que estou a pensar? "))

main()