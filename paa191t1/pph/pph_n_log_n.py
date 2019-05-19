from paa191t1.pph import HiperbolicSet


def pph_n_lg_n(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    # Utiliza TimSorte com complexidade n log n para ordenar os pares pela razao do maior para o menor
    n.sort(key=lambda x: x.r, reverse=True)
    i = 0
    while i < len(n):
        t = n[i]
        i += 1
        if t.r > s.r:
            s.add(t)
        else:
            i = len(n)
    return s
