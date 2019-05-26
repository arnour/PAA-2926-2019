
from paa191t1.pph import HiperbolicSet
from paa191t1.pph.utils import custom_pivot


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
    k = []
    a = t0.a
    b = t0.b
    # Na primeira iteração, considera todos os elementos de n
    # essa razão só tende a aumentar. O(n)
    for item in n:
        k.append(item)

    while len(k) > 0:
        # Encontra como pivot o elemento através da razão = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn))
        pivot = custom_pivot(k, None, t0.a, t0.b)
        a__ = a
        b__ = b

        lower_bounds = []
        equal_bounds = []
        upper_bounds = []

        # Percorre k usando o pivot para fazer o particionamento. Como na primeira iteração k==n, temos O(n)
        for element in k:
            if element < pivot:
                lower_bounds.append(element)
            elif element == pivot:
                equal_bounds.append(element)
                a__ += element.a
                b__ += element.b
            else:
                upper_bounds.append(element)
                a__ += element.a
                b__ += element.b

        # Caso o elemento pivot seja menor que o acumulado voltamos ao loop usando somente os
        # upper_bounds para não incluir os elementos iguais ao elemento pivot em s.
        if len(upper_bounds) > 0 and ((a__ / b__) > pivot.r):
            k = upper_bounds
        else:
            # Inclui os elementos maiores que o pivot em s.
            s.add_all(upper_bounds)

            # Precisamos verificar também nos lower_bounds se existem outros elementos que deveriam entrar na
            # lista s.
            if len(lower_bounds) > 0:
                max_of_lowers = max(lower_bounds)
                # Se o maior dos elementos tiver uma razão maior que a acumulada, quer dizer que realmente
                # existem mais elementos que estão no lower_bounds que devem entrar na lista s.
                if max_of_lowers.r > (a__ / b__):
                    # Fazemos o k ser só o lower_bounds, já que já adicionamos o resto, e repetimos o loop
                    # com o k reduzido.
                    k = lower_bounds
                    a = a__
                    b = b__
                else:
                    break
            else:
                break
    return s
