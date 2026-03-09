def farthest_first_last(lst):
    first_seen = {}
    max_dist = -1
    best_start_idx = -1
    result = None

    for i, num in enumerate(lst):
        if num not in first_seen:
            first_seen[num] = i
        start_idx = first_seen[num]
        dist = i - start_idx

        if dist > max_dist:
            max_dist = dist
            best_start_idx = start_idx
            result = (num, i)

        elif dist == max_dist:
            if start_idx < best_start_idx:
                best_start_idx = start_idx
                result = (num, i)

    return result

def main():
    lst = [1, 22, 2, 44, 3, 5, 22, 5, 22, 6, 44, 7] 
    resultado = farthest_first_last(lst)

    print(f"Lista: {lst}")
    print(f"Resultado: {resultado}")

    lst2 = [10, 20, 30]
    print(f"\nLista 2: {lst2}")
    print(f"Resultado: {farthest_first_last(lst2)}")

if __name__ == "__main__":
    main()