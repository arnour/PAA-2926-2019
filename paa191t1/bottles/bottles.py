def max_trials(max_height, test_bottles):
    """Returns the max trial number for the experiment in function of max_height and test_bottles.

    Args:
        max_height (long): A altura máxima
        test_bottles (int): O número de frascos que podem ser utilizados para testar

    Returns:
        (int) max trial number
    """
    return round(test_bottles * (max_height**(1.0 / test_bottles)))


def check_point_height(start, end, test_bottles):
    """Returns the size of each partition to be checked

    Returns:
        (int) check point size
    """
    return round(((end - start)**(test_bottles - 1))**(1 / test_bottles))


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

    break_point = int(break_point, 2)
    max_height = int("1" * max_height, 2)
    step = check_point_height(start=0, end=max_height, test_bottles=test_bottles)
    trials = max_trials(max_height, test_bottles)
    found = False
    lower = used_trials = used_bottles = 0

    while not found and used_bottles < test_bottles and used_trials < trials:
        used_trials += 1
        upper = min(step + lower, max_height)
        if (step > 1) and (break_point <= upper):
            used_bottles += 1
            step = check_point_height(start=lower, end=upper, test_bottles=test_bottles - used_bottles)
        elif (step == 1) and (break_point == upper):
            used_bottles += 1
            found = True
        else:
            lower = upper

    return found, used_trials, used_bottles
