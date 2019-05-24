import math
from paa191t1.bottles.bit_array import BitArray

def bottles(max_height, test_bottles, break_point):
    """O algoritmo recebe a altura máxima, a número de frascos que podem ser utilizados nos testes e a altura que um frasco quebra.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Este algoritmo conta com duas restrições:

    - O número de frascos que temos disponíveis para os testes.
    - O número de tentativas no pior caso que podem ser executadas.

    Args:
        max_height (long): A altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar
        break_point (str): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    found = False
    used_trials = used_bottles = 0
    break_point_bits = BitArray(break_point)
    last_max_bits = max_bits = BitArray("1" * max_height)
    pow_bottles = math.log(test_bottles, 2)
    if not pow_bottles.is_integer():
        raise NotImplementedError(f"{test_bottles} need to be base 2")

    for i in range(int(pow_bottles), 1, -1):
        last_max_bits = max_bits
        len_break_point = break_point_bits.count()
        step = len_break_point // pow_bottles
        to_right = int(step * i)
        ref_bits = max_bits >> to_right
        used_trials += 1
        if ref_bits > break_point_bits:
            used_bottles += 1
            max_bits = ref_bits
    
    ## TODO: Fazer em bit
    break_int = int(break_point, 2)
    upper_int = int(max_bits.to01(), 2)
    lower_int = int(last_max_bits.to01(), 2)

    for i in range(lower_int, upper_int + 1):
        used_trials += 1
        if i >= break_int:
            used_bottles += 1
            found = True
            break

    return found, used_trials, used_bottles
