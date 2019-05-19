from paa191t1.pph import HiperbolicSet


def pph_n_2(n, t0):
    """
    O algoritmo recebe uma lista n com pares de coordenadas (a, b) e retorna uma lista s, somente com as
    coordenadas que juntas tenham uma razão máxima do tipo r = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn)).

    O algoritmo vai varrer a lista inteira tentando adicionar um par de coordenadas se a razão delas for maior
    que a razão de s e remover caso a razão da coordenada seja menor ou igual a de s. Com isso, o algoritmo
    percorre no máximo O(n2) vezes para adicionar e remover todos os elementos da lista s porque precisa verificar
    se os elementos estão na lista s.

        Args:
        n (list[Pair]): Lista com coordenadas do tipo Pair.
        t0 (Pair): a0 e b0 iniciais de referência para o algoritmo.

    Returns:
        s (list[Pair]): Lista com coordenadas que maximizam a razão r.
    """
    s = HiperbolicSet(t0.a, t0.b)
    # Percorre toda a lista n, se a razão for maior que a da lista s e as coordenadas não estão na
    # lista s, adiciona na lista s.
    for t in n:  # O(n)
        index = s.index(t)  # O(s)
        if index == -1 and t.r > s.r:
            s.add(t)
    
    # Se a coordenada já estiver na lista s e a razão for menor que a razão da lista s,
    # então remove da lista.
    i = 0
    while i < len(s):  # O(s)
        t = s[i]
        i += 1
        index = s.index(t)  # O(s)
        if index > -1 and t.r <= s.r:
            s.remove(index)
            i = 0
    return s