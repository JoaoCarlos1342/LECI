
def primesUpTo(n):
    """
    Devolve um conjunto com todos os números primos até n
    usando o Crivo de Eratóstenes.
    """
    # 1. Comece com o conjunto {2, 3, ..., n}
    primes = set(range(2, n + 1))

    # Vamos iterar de 2 até a raiz quadrada de n.
    # Não precisamos ir além disso porque começamos a cortar a partir de i*i.
    # Se i*i for maior que n, o loop termina.
    limit = int(n**0.5)

    for i in range(2, limit + 1):
        # 2. Verifique se o número ainda está no conjunto (se não foi eliminado)
        if i in primes:
            # 3. Elimine os múltiplos de i a começar em i²
            # range(start, stop, step) gera: i², i²+i, i²+2i, ...
            multiples = range(i * i, n + 1, i)
            
            # Remove esses múltiplos do conjunto de primos
            primes.difference_update(multiples)

    return primes

def main():
    """ # Testing:
    s = primesUpTo(1000)
    print(s) """

    n = int(input("Diz um número e eu vou calcular quantos primos tem até esse número: "))
    print("Esta é a lista de números primos")
    primos = primesUpTo(n)
    print(sorted(primos))
    n_primos = len(primos)
    print("Há {} números primos até {}".format(n_primos, n))


    """ # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!") """

if __name__ == "__main__":
    main()

