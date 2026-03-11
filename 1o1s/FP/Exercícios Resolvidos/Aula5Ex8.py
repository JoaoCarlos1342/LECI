def evenThenOdd(string):
    even = string[::2]
    odd = string[1::2]
    all = even + odd

    return "".join(all)

def shortner(string):
    if len(string) == 0:
        return ""

    resultado = string[0]

    for char in string[1:]:
        if char != resultado[-1]:
            resultado += char
            
    return resultado

def repetidor(num):
    lista = []
    for numero in range(1, num + 1):
        for _ in range(numero):
            lista.append(numero)
            
    return lista

def maximus(lista):
    max = 0
    max_num = lista[0]
    for i in range(len(lista)):
        if lista[i] > max_num:
            max = i
            max_num = lista[i]

    return max

def main():
    string = input("Palavra: ")
    print(evenThenOdd(string))

    string = "Mississippi"
    print(f"Original: {string}")
    print(f"Resultado: {shortner(string)}")

    # Teste extra
    string2 = "AAABBBCCCA"
    print(f"Original: {string2} -> Resultado: {shortner(string2)}")

    num = int(input("Número: "))
    print(repetidor(num))

    lista = [7,9,2,0,5,4]
    print(maximus(lista))

main()