# Compute trigonometric functions with Taylor series.
# See: https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions

import math
import fatorial

def sin_a(x):
    #Return approximation to sin x using Taylor Series.
    soma = 0
    N = 25  # Número de termos da série (precisão)
    
    for i in range(N):
        denominador = 2 * i + 1
        
        # Calcula o termo atual
        # Nota: Usei math.factorial para garantir que funciona, 
        # mas podes usar fatorial.fatorial se o teu ficheiro estiver correto.
        numerador = ((-1)**i) * (x**denominador)
        termo = numerador / fatorial.fatorial(denominador)
        
        # Adiciona o termo à soma total
        soma = soma + termo
        
    return soma


# Constants
PI2 = math.pi * 0.5         # pi/2


def sin(x):
    """Return the sine of x."""
    # Use periodicity and simmetries of the sine function to reduce the
    # computation of sin x to the computation of sin r with 0 <= r <= pi/2.
    
    # Reduce
    n, r = divmod(x, PI2)    # x = n*pi/2 + r
    q = int(n) % 4           # quadrant

    # Approximate & Reconstruct
    if q == 0:
        s = sin_a(r)
    elif q == 1:
        s = sin_a(PI2 - r)
    elif q == 2:
        s = -sin_a(r)
    else: # q == 3
        s = sin_a(r - PI2)
    return s


def main():
    # Prints the values of sine computed by my function and Python's math.sin.
    print(f"{'angle':>5s} {'mysin':>19s} {'pysin':>19s} {'error':>19s}")
    for angle in range(0, 90+1, 15):  # angle in degrees
        x = math.radians(angle)
        mysin = sin(x)
        pysin = math.sin(x)
        error = mysin - pysin
        print(f"{angle:5d} {mysin:19.16f} {pysin:19.16f} {error:19.16f}")


if __name__ == "__main__":
    main()

