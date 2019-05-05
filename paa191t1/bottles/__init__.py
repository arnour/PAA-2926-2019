def max_trials(max_height, test_bottles):
    """Returns the max trial number for the experiment in function of max_height and test_bottles.

    Args:
        max_height (long): A altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar

    Returns:
        (int) max trial number
    """
    return round(test_bottles * (max_height**(1.0 / test_bottles)))


def bottles(max_height, test_bottles, break_point):
    """O algoritmo recebe a altura máxima, a número de frascos que podem ser utilizados nos testes e a altura que um frasco quebra.

    Com essas informações o algoritmo tenta encontrar a altura de quebra de maneira ótima respeitando as restrições.

    Este algoritmo conta com duas restrições:

    - O número de frascos que temos disponíveis para os testes.
    - O número de tentativas no pior caso que podem ser executadas.

    Args:
        max_height (long): A altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar
        break_point (long): A altura onde o frasco quebra de fato. Portanto, a altura a ser encontrada.

    Returns:
        int, int: Quantas tentativas foram feitas e quantos frascos foram utilizados
    """

    return 0, 0
