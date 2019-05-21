from paa191t1.bottles.bit_array import BitArray


def bottles(max_height, break_point):
    """O algoritmo recebe o número de bits e a altura que um frasco quebra em bits.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Este algoritmo conta com uma restrição:

    - O número de tentativas no pior caso que podem ser executadas.

    Args:
        max_height (long): O número de bits que representa a altura máxima
        break_point (str): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    decimal_break_point = int(break_point, 2)
    used_trials = used_bottles = 0
    upper_bound = int(max_height * "1", 2)
    lower_bound = 0
    pivot = upper_bound // 2
    found = False

    while not found:
        used_trials += 1
        if pivot > decimal_break_point:
            used_bottles += 1
            upper_bound = pivot - 1
            print(pivot, decimal_break_point, upper_bound, lower_bound)

        elif pivot < decimal_break_point:
            lower_bound = pivot + 1 
            print(pivot, decimal_break_point, upper_bound, lower_bound)
    
        else:
            used_bottles += 1
            found = True
        pivot = (upper_bound + lower_bound) // 2

    return found, used_trials, used_bottles
