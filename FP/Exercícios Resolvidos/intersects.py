"""
Considere que a, b são os extremos de um intervalo real [a, b[
e que c, d são os extremos de outro intervalo [c, d[.

Complete a definição da função abaixo para verificar
se os intervalos se itersectam.
Admita que a < b e c < d.
"""
def intersects(a, b, c, d):
    if c > b:
        intersection = False
    elif d < a:
        intersection = False
    else:
        intersection = True
    return intersection


def testIntersects(a, b, c, d, expected):
    """Call intersects, print result and check against expected result."""
    print(f"intersects({a}, {b}, {c}, {d})", end=" ")

    result = intersects(a, b, c, d)  # <-- Chamada à função!

    check = "OK" if result == expected else "FAIL"
    print(f"--> {result}    {check}")


def main():
    testIntersects(1, 6, 4, 8,  True)
    testIntersects(1, 6, 3, 5,  True)
    testIntersects(1, 6, 7, 8,  False)
    # Acrescente mais casos de teste...

    a = int(input("Qual é o primeiro número do primeiro intervalo? "))
    b = int(input("Qual é o segundo número do primeiro intervalo? "))
    c = int(input("Qual é o primeiro número do segundo intervalo? "))
    d = int(input("Qual é o segundo número do segundo intervalo? "))

    if intersects(a, b, c, d) == True:
        print("O intervalo [{}, {}[ intersecta o intervalo [{}, {}[".format(a, b, c, d))
    else:
        print("O intervalo [{}, {}[ não intersecta o intervalo [{}, {}[".format(a, b, c, d))

main()

