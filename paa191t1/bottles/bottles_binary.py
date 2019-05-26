from paa191t1.bottles.bit_array import BitArray


def get_next_bit(bit_array):
    """Pega próximo bit de forma sequencial.
    Args:
        bit_array (BitArray): BitArray inicial que deve ter seu valor de volta.

    Returns:
        (BitArray) pŕoximo número representado em array de bit.
    """
    # Se último elemento for zero, troca por um
    if not bit_array[-1]:
        bit_array[-1] = True
    # Senão, precisa encontrar o maior índice false e trocar todos os antes dele por false.
    else:
        bit_array.reverse()
        index = bit_array.index(False)
        for i in range(index):
            bit_array[i] = False
        # Depois trocar ele por true.
        bit_array[index] = True
        bit_array.reverse()
    return bit_array


def turn_next_bit_to_true(bit_array, binary=True):
    # Caso esteja utilizando a busca binária
    if binary:
        first_bit = bit_array.length() - 1
        # Pega o bit mediano
        middle_bit = first_bit // 2
        try:
            # Verifica se existe algum bit com true,
            first_true = bit_array.index(True)
        except ValueError:
            # senão devolve o próprio array de bit com true no final.
            bit_array[-1] = True
            return bit_array
        try:
            # Verifica se existe um bit falso no range entre o bit mediano e o primeiro verdadeiro.
            # Se não existir estoura ValueError
            last_middle = alternative_middle = bit_array.index(False, first_true, middle_bit + 1)
            # Se existir, itera até encontrar a próxima posição mediana entre o último
            # bit trocado para verdadeiro e o maior bit verdadeiro.
            while bit_array[middle_bit] and last_middle != middle_bit:
                # É possível que a busca não encontre mais um valor mediano, então precisamos
                # validar para sair do loop
                last_middle = middle_bit
                middle_bit = (first_true + middle_bit) // 2
            # Se a busca não encontrar um valor mediano, usamos o valor de index encontrado antes
            # e alteramos o bit
            if last_middle == middle_bit:
                bit_array[alternative_middle] = True
            # Senão alteramos o bit encontrado
            else:
                bit_array[middle_bit] = True
        except ValueError:
            # Caso não tenha um bit falso entre o mediano e o primeiro, vamos para os menores que o mediano
            try:
                middle_bit = bit_array.index(False, first_true)
            except ValueError:
                # Caso não exista um menor que o mediano, significa que encontramos a posição de quebra
                # e alteramos os maiores bits para poder tratar isso na função principal
                middle_bit = bit_array.index(False)
            bit_array[middle_bit] = True
    # Senão faz de forma sequencial invertendo sempre o menor bit falso.
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

    max_ref_bits.reverse()
    to_right = max_ref_bits.index(True)
    max_ref_bits.reverse()

    # Vamos pulando em steps de baixo para cima para tentarmos encontrar o primeiro
    # range que quebra
    while ref_bits != max_bits and (test_bottles - used_bottles) > 1 and not found:
        # Se ainda deve fazer deslocamento para a direita, vai diminuindo gradativamente
        # o tamanho do array de bit
        if to_right > 0:
            # cada vez desloca menos para a direita para achar aonde o frasco quebra
            to_right -= 1
            ref_bits = max_ref_bits >> to_right
            used_trials += 1
            # se o frasco quebrar, não devemos mais deslocar para a direita
            if ref_bits >= break_point_bits:
                used_bottles += 1
                max_ref_bits = ref_bits
                to_right = 0
            # Senão, continuamos a deslocar e vamos atualizando o valor mínimo que pode ser
            else:
                min_bits = ref_bits.copy()

        # Se já achamos o range que o frsco quebra, então vamos trocando os zeros por um a direita
        # do primeiro bit que tenha 1
        else:
            binary = False
            # Caso o número de frascos seja menor que 2 podemos trocar os zeros como uma busca binária
            if (test_bottles - used_bottles) > 2:
                binary = True
            used_trials += 1
            # Aqui convertemos os bits com zero sequencialmente ou como busca binaria
            ref_bits = turn_next_bit_to_true(min_bits.copy(), binary)

            # No caso em que os arrays de bit de mínimo e máximo são iguais ao de referência,
            # ou quando o ref_bits passou de max_ref_bits então achamos o valor sem precisar
            # fazer um teste.
            if max_ref_bits <= ref_bits and min_bits == ref_bits:
                found = True
                used_trials -= 1
            # Se o valor de referência é maior, quebramos a garrafa e colocamos um novo topo
            elif ref_bits >= break_point_bits:
                used_bottles += 1
                max_ref_bits = ref_bits
            # Senão atualizamos o mínimo com a referência
            else:
                min_bits = ref_bits.copy()

    # Parte sequencial do código
    while min_bits <= max_bits and not found:
        # Varre sequencialmente o que sobrou entre o número mínimo e máximo de bits
        used_trials += 1
        if min_bits.count() == 0:
            min_bits = get_next_bit(min_bits.copy())

        # Quando for igual dizemos que encontramos, porque estamos andando sequencialmente
        if min_bits == break_point_bits:
            used_bottles += 1
            found = True
        # Senão atualizamos o mínimo pro próximo número
        else:
            min_bits = get_next_bit(min_bits.copy())

    return found, used_trials, used_bottles
