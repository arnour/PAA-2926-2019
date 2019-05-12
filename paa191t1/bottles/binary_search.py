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

    found = False
    used_trials = used_bottles = 0
    break_point_bits = BitArray(break_point)

    # usamos como referência inicial 10000 porque é o meio da sequência máxima de bits
    ref_bits = BitArray("1" + (max_height - 1) * "0")
    # precisamos controlar como os 1 e zeros vão se movendo nas iterações
    one_to_move = zero_to_change = 1

    while not found:
        used_trials += 1
        # se for quebrou a garrafa e só tiver 1 bit com True no array de bits. Ex: 010000
        if ref_bits > break_point_bits and sum(ref_bits.tolist()) == 1:
            used_bottles += 1
            # ao deslocar o bit para a direita dividimos o número que o array de bits representa na metade
            ref_bits = ref_bits >> 1
            zero_to_change += 1

        elif ref_bits > break_point_bits:
            # aqui vamos decrementando dentro de um range menor os bits em potência de 2.
            used_bottles += 1
            ref_bits[one_to_move] = False
            ref_bits[one_to_move + 1] = True
            one_to_move += 1
            zero_to_change = one_to_move

        elif ref_bits == break_point_bits:
            # encontramos a posição ótima aonde o frasco quebra.
            used_bottles += 1
            found = True

        else:
            # nesse caso a garrafa não quebra, então tentamos aumentar um pouco o número para que quebre.
            # para aumentar o número como na busca binária em potência de 2, precisamos colocar o
            # segundo maior bit que ainda estava como False como True.
            ref_bits[zero_to_change] = True
            one_to_move = zero_to_change
            zero_to_change += 1

    return found, used_trials, used_bottles
