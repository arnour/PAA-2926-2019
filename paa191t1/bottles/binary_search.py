from paa191t1.bottles.bit_array import BitArray

def get_before_bit(bit_array):
    if bit_array[-1] == True:
        bit_array[-1] = False
    else:
        bit_array.reverse()
        index = bit_array.index(True)
        for i in range(index):
            bit_array[i] = True
        bit_array[index] = False
        bit_array.reverse()
    return bit_array

def bottles(max_height, break_point):
    """O algoritmo recebe o número de bits e a altura que um frasco quebra em bits.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Args:
        max_height (long): O número de bits que representa a altura máxima
        break_point (str): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    found = False
    used_trials = used_bottles = 0
    break_point_bits = BitArray(break_point)

    # usamos como referência inicial 0111111 porque é o meio da sequência máxima de bits
    ref_bits = BitArray("0" + (max_height - 1) * "1")
    # precisamos controlar como os 1 e zeros vão se movendo nas iterações
    one_to_move = zero_to_change = 0

    while not found:
        used_trials += 1

        if ref_bits.all() or (ref_bits.count() == 0):
            # Não precisamos gastar uma tentativa ou garrafa aqui porque estão nas pontas 
            # e são os últimos números que a busca binária vai testar
            used_trials -= 1
            found = True

        elif ref_bits >= break_point_bits:
            # se for quebrou a garrafa
            used_bottles += 1
            before_ref = get_before_bit(ref_bits.copy())
            
            used_trials += 1
            if before_ref < break_point_bits:
                # encontramos a posição ótima aonde o frasco quebra.
                found = True
                continue
            else:
                used_bottles += 1

            # se só tiver 1 bit com True no array de bits. Ex: 010000
            if ref_bits.count() == 1:
                # ao deslocar o bit para a direita dividimos o número que o array de bits representa na metade
                ref_bits = ref_bits >> 1
                zero_to_change += 1
                one_to_move = zero_to_change            
            # aqui vamos decrementando dentro de um range menor os bits em potência de 2.
            else:
                one_to_move += 1
                ref_bits[one_to_move] = False
                zero_to_change = one_to_move

        elif ref_bits < break_point_bits:
            # nesse caso a garrafa não quebra, então tentamos aumentar um pouco o número para que quebre.
            # para aumentar o número como na busca binária em potência de 2, precisamos colocar o
            # segundo maior bit que ainda estava como False como True.
            ref_bits[zero_to_change] = True
            zero_to_change += 1
            one_to_move = zero_to_change
            if ref_bits.length() > one_to_move:
                ref_bits[one_to_move] = False

    return found, used_trials, used_bottles
