from paa191t1.bottles.bit_array import BitArray


def bottles(max_height, test_bottles, break_point):
    """O algoritmo recebe o número de bits, o número de frascos que podem ser utilizados nos testes e a altura que um frasco quebra em bits.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Este algoritmo conta com duas restrições:

    - O número de frascos que temos disponíveis para os testes.
    - O número de tentativas no pior caso que podem ser executadas.

    Args:
        max_height (long): O número de bits que representa a altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar
        break_point (str): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    found = False
    used_trials = used_bottles = 0
    max_bits = BitArray(max_height * "1")
    roll_zero = max_bits.length() + 1
    # trials = max_bits.length()
    break_point_bits = BitArray(break_point)
    min_bits = ref_bits = BitArray((max_height - 1) * "0" + "1")

    if BitArray(max_height * "0") == break_point_bits:
        used_bottles += 1
        return True, used_trials, used_bottles

    while not found:
        used_trials += 1
        if ref_bits < break_point_bits:

            min_bits = ref_bits
            ref_bits = ref_bits << 1
            ref_bits[-1] = True

        else:
            max_bits = ref_bits
            used_bottles += 1
            zero_index = ref_bits.length() - 1
            while not found:
                used_trials += 1
                if ref_bits == break_point_bits:
                    used_bottles += 1
                    found = True
                elif ref_bits > break_point_bits:
                    max_bits = ref_bits
                    used_bottles += 1
                    ref_bits[zero_index - 1] = True
                    ref_bits[zero_index] = False
                    zero_index -= 1
                else:
                    print("falta fazer")





    return found, used_trials, used_bottles
