from paa191t1.pph import Pair


def median_bounds(K, compare):
    lt_compare = []
    eq_to_compare = []
    gt_compare = []
    for element in K:
        if element < compare:
            lt_compare.append(element)
        elif element == compare:
            eq_to_compare.append(element)
        else:
            gt_compare.append(element)

    return lt_compare, eq_to_compare, gt_compare


def median_of_medians(L, k=None, *args, **kwargs):
    """
    Pega o elemento mediano em uma lista em O(n)
    """
    k = k or len(L) // 2

    if (len(L) <= 5):
        # Caso só tenham 5 elementos retorna os elementos ordenados
        return sorted(L)[k]

    sublists = []
    for index in range(0, len(L), 5):
        # Cria várias listas com 5 elementos cada
        sublists.append(L[index:index + 5])

    medians = []
    for sublist in sublists:
        # Pega o elemento mediano de cada lista de 5 elementos
        medians.append(median_of_medians(sublist, (len(sublist) - 1) // 2))

    # Calcula o elemento mediano de cada mediana das listas de 5 elementos
    mom = median_of_medians(medians, (len(medians) - 1) // 2)

    # Verifica elementos maiores, menores e iguais a mediana.
    lt_mom, eq_to_mom, gt_mom = median_bounds(L, mom)

    if (k < len(lt_mom)):
        # Caso o índice k do elemento seja menor ou igual a lista de menores que ele,
        # significa que ele ainda pode explorar a menor lista para encontrar a mediana.
        return median_of_medians(lt_mom, k)
    elif (k > (len(lt_mom) + len(eq_to_mom))):
        # Caso o índice k seja maior que o tamanho da lista de menores somado com o tamanho
        # da lista de iguais a ele, então ele precisa explorar items maiores que ele na lista
        # de maiores itens.
        return median_of_medians(gt_mom, k - len(lt_mom) - len(eq_to_mom))
    else:
        return mom  # Sendo igual retorna a própria mediana das medianas


def custom_pivot(L, k=None, a0=0, b0=0):
    """
    Calcula um pivot customizado em O(n)
    """
    sum_a = a0
    sum_b = b0
    for pair in L:
        sum_a += pair.a
        sum_b += pair.b
    return Pair(sum_a, sum_b)
