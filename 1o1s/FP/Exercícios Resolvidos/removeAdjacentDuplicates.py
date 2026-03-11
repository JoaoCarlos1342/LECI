def remove_adjacent_duplicates(word):
    if not word:
        return word

    result = [word[0]]  # Começa com a primeira letra

    for char in word[1:]:
        if char != result[-1]:  # Só adiciona se for diferente da anterior
            result.append(char)

    return ''.join(result)


# Exemplo
print(remove_adjacent_duplicates("Mississipi"))  # Misisipi
