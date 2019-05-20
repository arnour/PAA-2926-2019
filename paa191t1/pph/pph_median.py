from paa191t1.pph import HiperbolicSet
from paa191t1.pph.utils import median_of_medians, median_bounds


def pph_median(n, t0, pivot_function=median_of_medians):
    """
    O algoritmo recebe uma lista n com pares de coordenadas (a, b) e retorna uma lista s, somente com as
    coordenadas que juntas tenham uma razão máxima do tipo r = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn)).

    Esse algoritmo dá somente uma passada na lista n O(n) verificando o que deve estar na lista s através de um pivot.
    No caso como padrão utiliza a mediana das medianas.

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
    # Fica só com elementos que tenham uma razão maior que a razão inicial porque
    # essa razão só tende a aumentar. O(n)
    for item in n:
        if item.r > t0.r:
            k.append(item)

    execute = True
    while execute and len(k) > 0:
        execute = False

        # Encontra como pivot o elemento mediano
        pivot = pivot_function(k)

        # Faz comparativo dessa mediana com todos os elementos da lista. O(n)
        lower_bounds, equal_bounds, upper_bounds = median_bounds(k, pivot)
        a__ = a
        b__ = b

        # Acumula os elementos maiores e iguais ao elemento mediano para comparar com a razão
        for t in (upper_bounds + equal_bounds):
            a__ += t.a
            b__ += t.b

        # Caso o elemento mediano seja menor que o acumulado voltamos ao loop usando somente os
        # upper_bounds para não incluir os elementos iguais ao elemento mediano em s.
        if len(upper_bounds) > 0 and ((a__ / b__) > pivot.r):
            k = upper_bounds
            execute = True
            continue

        # No caso da razão dos elementos medianos serem maiores, eles são incluídos na lista final também.
        s.add_all(upper_bounds + equal_bounds)

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
                execute = True
                continue
    return s
