from paa191t1.pph import HiperbolicSet


def pph_n_lg_n(n, t0):
    """
    O algoritmo recebe uma lista n com pares de coordenadas (a, b) e retorna uma lista s, somente com as
    coordenadas que juntas tenham uma razão máxima do tipo r = ((a0 + a1 + ... + an) / (b0 + b1 + ... + bn)).

    Primeiramente o algoritmo ordena do maior para o menor as cordenadas com base na razão delas com
    O(nlogn) e depois varre toda a lista O(n) buscando somente elementos que maximizem a razão r.

        Args:
        n (list[Pair]): Lista com coordenadas do tipo Pair.
        t0 (Pair): a0 e b0 iniciais de referência para o algoritmo.

    Returns:
        s (list[Pair]): Lista com coordenadas que maximizam a razão r.
    """
    s = HiperbolicSet(t0.a, t0.b)
    # Utiliza TimSorte com complexidade O(nlogn) para ordenar os pares pela razao do maior para o menor.
    n.sort(key=lambda x: x.r, reverse=True)
    i = 0
    # Busca na lista elementos que maximizem a razão r.
    while i < len(n):
        t = n[i]
        i += 1
        if t.r > s.r:
            # Compara as razões dos das coordenadas com a razão de s atual e adiciona a lista se ela for maior.
            s.add(t)
        else:
            # Caso o próximo não seja maior que a razão atual, podemos parar porque todos os outros
            # são menores e só vão colaborar para diminuir ou estabilizar a razão de s.
            break
    return s
