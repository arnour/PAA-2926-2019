from paa191t1.bottles.bit_array import BitArray
import math



def get_next_bit(bit_array):
    if bit_array[-1] == False:
        bit_array[-1] = True
    else:
        bit_array.reverse()
        index = bit_array.index(False)
        for i in range(index):
            bit_array[i] = False
        bit_array[index] = True
        bit_array.reverse()
    return bit_array

def turn_next_bit_to_true(bit_array, binary=True):
    if binary:
        first_bit = bit_array.length() - 1
        middle_bit = first_bit // 2
        first_true = bit_array.index(True)
        try:
            last_middle = alternative_middle = bit_array.index(False, first_true, middle_bit + 1)
            while bit_array[middle_bit] == True and last_middle != middle_bit:
                last_middle = middle_bit
                middle_bit = (first_true + middle_bit) // 2
            if last_middle == middle_bit:
                bit_array[alternative_middle] = True
            else:
                bit_array[middle_bit] = True            
        except ValueError:
            bit_array.reverse()
            middle_bit = bit_array.index(False)
            bit_array[middle_bit] = True
            bit_array.reverse()
        print(bit_array, middle_bit, first_bit)
    else:
        bit_array.reverse()
        index = bit_array.index(False)
        bit_array[index] = True
        bit_array.reverse()
    return bit_array

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
    max_bits = BitArray("1" * max_height)
    max_ref_bits = BitArray("1" + (max_height - 1) * "0")
    ref_bits = min_bits = BitArray("0" * max_height)
    
    step = int(math.log((test_bottles - used_bottles), 2))
    max_ref_bits.reverse()
    to_right = len_max_bits = max_ref_bits.index(True)
    max_ref_bits.reverse()

    # Vamos pulando em steps de baixo para cima para tentarmos encontrar o primeiro
    # range que quebra
    while ref_bits != max_bits and (test_bottles - used_bottles) > 1:
        if to_right == 0:
            binary = False
            if (test_bottles - used_bottles) > 2:
                binary = True
            used_trials += 1
            ref_bits = turn_next_bit_to_true(min_bits.copy(), binary)
            if ref_bits >= break_point_bits:
                used_bottles += 1
                max_ref_bits = ref_bits
                step = int(math.log((test_bottles - used_bottles), 2))
            else:
                min_bits = ref_bits.copy()

        else:
            to_right -= 1
            ref_bits = max_ref_bits >> to_right
            print(max_ref_bits, min_bits, ref_bits, step, to_right)
            used_trials += 1
            if ref_bits >= break_point_bits:
                used_bottles += 1
                max_ref_bits = ref_bits
                max_ref_bits.reverse()
                len_max_bits = max_ref_bits.index(True)
                max_ref_bits.reverse()
                step = int(math.log((test_bottles - used_bottles), 2))
            else:
                min_bits = ref_bits.copy()

    # Parte sequencial do código
    while min_bits <= max_bits and not found:
        # Varre sequencialmente o que sobrou entre o número mínimo e máximo de bits
        used_trials += 1
        if min_bits.count() == 0:
            min_bits = get_next_bit(min_bits.copy())
        if min_bits == break_point_bits:
            # Quando for igual dizemos que encontramos, porque estamos andando sequencialmente
            used_bottles += 1
            found = True
        else:
            min_bits = get_next_bit(min_bits.copy())

    return found, used_trials, used_bottles
