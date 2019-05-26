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


def turn_next_bit_to_true_or_false(bit_array, upper, next_index=0):
    """Pega próximo bit de acordo com o next_index e se deve ir para cima e para baixo e troca o valor dele.
    Args:
        bit_array (BitArray): BitArray inicial que deve ter seu valor de volta.
        upper (bool): se seve continuar aumentando o valor.
        next_index (int): índice do próximo número que deve ser alterado.

    Returns:
        (BitArray) pŕoximo número representado em array de bit.
    """
    # trabalhamos sempre com os bits ao contrário
    bit_array.reverse()
    # Se deve subir o número então só transforma o próximo zero em um.
    if upper:
        index = bit_array.index(False)
        bit_array[index] = True
    # Se deve descer o número, devemos escolher entre descer todos os bits para zero 
    # ou somente a partir do contador
    else:
        indexes = bit_array.search(BitArray("10"))
        # Caso exista essa sequência, vamos usar ela como next_index e alterar os zeros de dentro
        if len(indexes) > 0:
            index = bit_array.length()
            normal_next_index = index - indexes[0]
            # Caso o next_index seja maior que o índice encontrado significa que devemos continuar
            # andando até encontrar o próximo bit que deve virar zero.
            if next_index >= normal_next_index:
                next_index = next_index + 1
            # Senão usa o próprio índice encontrado
            else:
                next_index = normal_next_index
            # Altera todos abaixo do índice para zero
            for i in range(index - next_index):
                bit_array[i] = False
        # Se não existir a sequência, provavelmente tudo é 1 e devemos decrementar a partir dele
        else:
            try:
                # Se não for tudo um, então estamos com uma subsequência cheia de verdadeiros
                index = bit_array.index(False)
            except ValueError:
                # Se for tudo verdadeiro, então pega o primeiro elemento (equivalente ao tamanho no inverso)
                next_index += 1
                index = bit_array.length()
            # Troca tudo para zero embaixo do índice verdadeiro encontrado
            for i in range(index - 1 - next_index):
                bit_array[i] = False
    bit_array.reverse()

    return bit_array, next_index


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
    upper = True
    next_index = 0
    # Vamos pulando em steps de baixo para cima para tentarmos encontrar o primeiro
    # range que quebra
    while (test_bottles - used_bottles) > 1 and not found:
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
                max_ref_bits = ref_bits.copy()
                to_right = 0
                ref_bits = min_bits.copy()
            # Senão, continuamos a deslocar e vamos atualizando o valor mínimo que pode ser
            else:
                min_bits = ref_bits.copy()

        # Se já achamos o range que o frsco quebra, então vamos trocando os zeros por um a direita
        # do primeiro bit que tenha 1
        else:
            # Caso o número de frascos seja menor que 2 podemos trocar os zeros como uma busca binária
            used_trials += 1
            # Aqui convertemos os bits com zero ou um sequencialmente de acordo com o next_index e se
            # deve aumentar ou diminuir 
            ref_bits, next_index = turn_next_bit_to_true_or_false(ref_bits.copy(), upper, next_index)

            # No caso em que os arrays de bit de mínimo e máximo são iguais ao de referência,
            # ou quando o ref_bits passou de max_ref_bits então achamos o valor sem precisar
            # fazer um teste.
            if max_ref_bits <= ref_bits and min_bits == ref_bits:
                found = True
                used_trials -= 1
            # Se o valor de referência é maior, quebramos a garrafa e colocamos um novo topo
            elif ref_bits >= break_point_bits:
                used_bottles += 1
                max_ref_bits = ref_bits.copy()
                upper = False
            # Senão atualizamos o mínimo com a referência
            else:
                upper = True
                min_bits = ref_bits.copy()
    # Parte sequencial do código
    while min_bits <= max_ref_bits and not found:
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
