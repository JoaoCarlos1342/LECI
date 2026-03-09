def mais_repetido_consecutivo(s):

    # Variáveis que guardam o melhor bloco encontrado até agora
    max_char = s[0]    # caracter que, até agora, tem o maior bloco consecutivo
    max_count = 1      # comprimento desse bloco máximo

    # Variáveis que guardam o bloco corrente que estamos a contar enquanto percorremos s
    atual_char = s[0]  # caracter do bloco corrente
    atual_count = 1    # comprimento do bloco corrente

    # Percorremos desde o segundo carácter até ao fim
    for i in range(1, len(s)):
        if s[i] == atual_char:
            # o carácter actual continua o mesmo bloco → incrementa o contador corrente
            atual_count += 1
        else:
            # encontrou-se um novo carácter — o bloco corrente terminou
            # comparamos o bloco terminado (atual_count) com o melhor conhecido (max_count)
            if atual_count > max_count:
                # Só atualizamos o "máximo" se for estritamente maior.
                # Isto garante que em caso de empate (atual_count == max_count)
                # **não** substituímos o max_char — assim o primeiro bloco mantém a preferência.
                max_count = atual_count
                max_char = atual_char

            # Reset para começar a contar o novo bloco que começou em s[i]
            atual_char = s[i]
            atual_count = 1

    # Depois do ciclo, ainda temos de verificar o último bloco (pois o ciclo só atualiza
    # o max quando encontra um carácter diferente; o último bloco pode ser o maior)
    if atual_count > max_count:
        max_count = atual_count
        max_char = atual_char

    return max_char

# Função main para poderes testar a função
def main():
    seq = input("Introduza a sequência: ")
    resultado = mais_repetido_consecutivo(seq)
    print("Caracter que mais se repete consecutivamente:", resultado)

main()
