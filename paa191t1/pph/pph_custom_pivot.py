from paa191t1.pph import HiperbolicSet
from paa191t1.pph.utils import custom_pivot
from paa191t1.pph import Pair


def pph_custom_pivot(n, t0):
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
    # for item in n:
    #     if item.r > t0.r:
    #         k.append(item)

    i = 0

    # passo 0:
    k = n
    pivot = custom_pivot(k, None, t0.a, t0.b)
    a_ = pivot.a
    b_ = pivot.b

    # passo 1:
    # print("\n\n")

    for i in k[:]:
        # print("===> bef: {}".format(k))
        # print("pivot.r >= i.r == {} >= {} {} ".format(str(pivot.r), str(i.r),(pivot.r >= i.r)))
        if pivot.r >= i.r:
            k.remove(i)
            a_ -= i.a
            b_ -= i.b
            pivot = Pair(a_, b_)
        # print("---> aft: {}".format(k))

    s.add_all(k)

    return s

    # passo 1:
    # while len(k) > 0:

    # while len(k) > 0:
    #     # Encontra como pivot o elemento mediano
    #     pivot = custom_pivot(k, None, t0.a, t0.b)
    #     i += 1

    #     # Faz comparativo dessa mediana com todos os elementos da lista. O(n)
    #     a1, b1, lower_bounds, equal_bounds, upper_bounds = median_bounds(k, pivot)
    #     a__ = a + a1
    #     b__ = b + b1
    #     # print("\n")
    #     # print("{}- pivot: {}".format(str(i), pivot))
    #     # print("{}- K: {}".format(str(i), k))
    #     # print("{}- lower_bounds: {}".format(str(i), lower_bounds))
    #     # print("{}- equal_bounds: {}".format(str(i), equal_bounds))
    #     # print("{}- upper_bounds: {}".format(str(i), upper_bounds))

    #     # Acumula os elementos maiores e iguais ao elemento mediano para comparar com a razão
    #     # for t in (upper_bounds + equal_bounds):
    #     #     a__ += t.a
    #     #     b__ += t.b

    #     # print("{}- (a__ / b__): {}".format(str(i), (a__ / b__)))
    #     # Caso o elemento mediano seja menor que o acumulado voltamos ao loop usando somente os
    #     # upper_bounds para não incluir os elementos iguais ao elemento mediano em s.
    #     if len(upper_bounds) > 0 and ((a__ / b__) > pivot.r):
    #         k = upper_bounds
    #     else:
    #         # No caso da razão dos elementos medianos serem maiores, eles são incluídos na lista final também.
    #         # s.add_all(upper_bounds + equal_bounds)
    #         s.add_all(upper_bounds)

    #         # Precisamos verificar também nos lower_bounds se existem outros elementos que deveriam entrar na
    #         # lista s.
    #         if len(lower_bounds) > 0:
    #             max_of_lowers = max(lower_bounds)
    #             # Se o maior dos elementos tiver uma razão maior que a acumulada, quer dizer que realmente
    #             # existem mais elementos que estão no lower_bounds que devem entrar na lista s.
    #             if max_of_lowers.r > (a__ / b__):
    #                 # Fazemos o k ser só o lower_bounds, já que já adicionamos o resto, e repetimos o loop
    #                 # com o k reduzido.
    #                 k = lower_bounds
    #                 a = a__
    #                 b = b__
    #             else:
    #                 break
    #         else:
    #             break
    # return s
