from paa191t1.bottles.bit_array import BitArray


def bottles(max_height, break_point):
    """O algoritmo recebe o número de bits e a altura que um frasco quebra em bits.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Args:
        max_height (long): O número de bits que representa a altura máxima
        break_point (str): A altura onde o frasco quebra de fato em bits. Portanto, a altura a ser encontrada.

    Returns:
        bool, int, int: encontrado, tentativas usadas, frascos usados
    """

    # Convertemos para decimal a entrada
    decimal_break_point = int(break_point, 2)
    max_bound = upper_bound = int(max_height * "1", 2)
    min_bound = lower_bound = 0
    used_trials = used_bottles = 0
    pivot = upper_bound // 2
    found = False

    while not found:
        used_trials += 1
        
        if (pivot == max_bound) or (pivot == min_bound):
            # Não precisamos gastar uma tentativa ou garrafa aqui porque estão nas pontas 
            # e são os últimos números que a busca binária vai testar
            used_trials -= 1
            found = True
            
        # Se quebrou a garrafa então é porque está a cima do breakpoint e precisamos
        # diminuir o upper_bound.
        elif pivot >= decimal_break_point:
            used_bottles += 1
            upper_bound = pivot - 1

            # Precisamos validar se o anterior quebra também. Se não quebrar, então achamos.
            # Quebrando continuamos a busca.
            used_trials += 1
            if (pivot - 1) < decimal_break_point:
                found = True
            else:
                used_bottles += 1

        # Caso não quebre só continuamos a busca aumentando o lower_bound
        elif pivot < decimal_break_point:
            lower_bound = pivot + 1

        # O pivot é sempre metade do upper_bound e lower_bound para garantir a propriedade
        # de busca binária.
        pivot = (upper_bound + lower_bound) // 2

    return found, used_trials, used_bottles
