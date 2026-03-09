def fibonacci(n):
    # Casos base definidos no enunciado
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Inicialização (equivalente a F0 e F1)
    a = 0  # F(n-2)
    b = 1  # F(n-1)
    
    # Começamos no 2 porque 0 e 1 já foram tratados
    # O loop vai até n (inclusive)
    for _ in range(2, n + 1):
        soma = a + b    # Calcula o novo termo
        
        # Atualiza os valores para a próxima iteração
        a = b           # O 'último' vira o 'penúltimo'
        b = soma        # O 'novo' vira o 'último'
        
    return b

def FibonacciLista(n):
    # Caso especial: se n for 0, a lista só tem o primeiro elemento
    if n == 0:
        return [0]
    
    # 1. Criar a lista com os iniciais
    sequencia = [0, 1]
    
    # 2. Ciclo de 2 até n
    for i in range(2, n + 1):
        # 3. Calcular o próximo valor somando os dois últimos da lista
        # sequencia[-1] é o último
        # sequencia[-2] é o penúltimo
        proximo_valor = sequencia[-1] + sequencia[-2]
        
        # Adicionar à lista
        sequencia.append(proximo_valor)
        
    # 4. Retornar a lista completa
    return sequencia

def main():
    num = int(input("Qual o indíce da sequência de Fibonacci? "))
    print(FibonacciLista(num))
    print(fibonacci(num))

main()