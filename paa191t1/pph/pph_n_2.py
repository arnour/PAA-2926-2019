from paa191t1.pph import HiperbolicSet


def pph_n_2(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    i = 0
    while i < len(n):
        t = n[i]
        i += 1
        index = s.index(t)
        if index == -1 and t.r > s.r:
            s.add(t)
            i = 0
        elif index > -1 and t.r <= s.r:
            s.remove(index)
            i = 0
    return s
