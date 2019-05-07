from bitarray import bitarray

def bottles(max_height, test_bottles, break_point):
    """O algoritmo recebe o número de bits, o número de frascos que podem ser utilizados nos testes e a altura que um frasco quebra em bits.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Este algoritmo conta com duas restrições:

    - O número de frascos que temos disponíveis para os testes.
    - O número de tentativas no pior caso que podem ser executadas.

    Args:
        max_height (long): O número de bits que representa a altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar
        break_point (long): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    found = False
    used_trials = used_bottles = 0
    max_bits = bitarray(max_height * "1")
    break_point_bits = bitarray(break_point)
    middle_bits = max_bits[:-1]
    last_bit = max_bits[-2:-1]
    while not found and used_bottles < test_bottles and used_trials < trials:
        used_trials += 1

        if middle_bits > break_point_bits:
            used_bottles -= 1
            last_bit = middle_bits[-2:-1]
            middle_bits = middle_bits[:-1]

        elif middle_bits < break_point_bits:
            middle_bits = middle_bits + last_bit.invert()

    return found, used_trials, used_bottles
