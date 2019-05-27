from paa191t1.pph import HiperbolicSet
from paa191t1.pph.utils import custom_pivot
from paa191t1.pph import Pair


def pph_custom_pivot(n, t0):
    """
    O algoritmo recebe uma lista n com pares de coordenadas (a, b) e retorna uma lista s, somente com as
    coordenadas que juntas tenham uma razão máxima do tipo r = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn)).

    Esse algoritmo tem complexidade de pior caso O(n^2) quando a razão de todos os elementos serão sempre menores que a razão
    do pivot. Para encontrar o elemento pivot, o algoritmo faz o seguinte cálculo:
    pivot = [a0 + (a1 + a2 + ... + an)] / [b0 + (b1 + b2 + ... + bn)]

        Args:
        n (list[Pair]): Lista com coordenadas do tipo Pair.
        t0 (Pair): a0 e b0 iniciais de referência para o algoritmo.

    Returns:
        s (list[Pair]): Lista com coordenadas que maximizam a razão r.
    """
    s = HiperbolicSet(t0.a, t0.b)
    k = n

    # 0- Calcula um pivot usando a função r = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn)) em O(n)
    pivot = custom_pivot(k, None, t0.a, t0.b)

    # 1- Chama os steps da recursão para o cálculo do pph customizado
    res = pph_steps(k, pivot, pivot.a, pivot.b)

    # 4- Adiciona a lista com os pares que maximizam a razão - O(n)
    s.add_all(res)

    return s


def pph_steps(k, p_pivot, a_, b_):
    """
    O algoritmo recebe uma lista k com pares de coordenadas (a, b) e retorna uma lista k_temp, somente com as
    coordenadas que juntas tenham uma razão máxima.

    Esse algoritmo tem complexidade de pior caso O(n^2) quando a razão de somente 1 elemento é pior que o pivot a cada
    iteração na recursão.

    Args:
        k (list[Pair]): Lista com coordenadas do tipo Pair.
        p_pivot: O elemento pivot (Pair) = [a0 + (a1 + a2 + ... + an)] / [b0 + (b1 + b2 + ... + bn)]
        a_: O valor acumulado [a0 + (a1 + a2 + ... + an)]
        b_: O valor acumulado [b0 + (b1 + b2 + ... + bn)]

    Returns:
        s (list[Pair]): Lista com coordenadas que maximizam a razão r.
    """

    k_temp = []
    pivot = p_pivot
    step_deep = False
    a = a_
    b = b_

    # 1- Percorre a lista k para eliminar pares de elementos cuja a razão seja menor que a razão do pivot
    for pair in k:
        if pivot.r >= pair.r:
            a -= pair.a
            b -= pair.b
            step_deep = True
        else:
            k_temp.append(pair)

    # 2- Caso tenha eliminado algum elemento, é necessário ir mais um nível na recursão
    if step_deep:
        pivot = Pair(a, b)
        # 3- Chama novamente o pph_steps para percorrer novamente os pares considerados
        return pph_steps(k_temp, pivot, a, b)

    else:
        return k_temp
