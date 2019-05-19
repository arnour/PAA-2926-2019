import logging
from paa191t1.pph import HiperbolicSet
from paa191t1.pph.utils import median_of_medians

logger = logging.getLogger("pph")


def pph_median(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    a = []
    b = []
    for t in n:
        a.append(t.a)
        b.append(t.b)
    k = list(range(len(n)))
    logger.debug(f'NNNNN {n}')
    logger.debug(f'KKKKKK {k}')
    nn = pph_med2(t0.a, t0.b, a, b, k)
    for i in nn:
        s.add(n[i])
    return s


def pph_med2(a0, b0, a, b, K):
    # passo 0
    I1 = []
    a_ = a0
    b_ = b0

    ab = [a[i] / b[i] for i in K]
    KK = []
    for k, i in enumerate(K):
        logger.debug(f'k,i :: ab[i] <= (a_ / b_) {k},{i} :: {ab[i]} -- {(a_ / b_)} ==> {ab[i] <= (a_ / b_)}')
        if ab[i] > (a_ / b_):
            KK.append(i)
    K = KK

    logger.debug(f'passo0: K : {K} // ab_ {ab} // {a0/b0}')

    def median(K, ab):
        logger.debug(f'K {K}, ab {ab}')
        abk = [ab[i] for i in K]
        m = median_of_medians(abk)
        logger.debug(f'm: {m}, ab: {ab}, ab.index == {ab.index(m)}')
        return ab.index(m)

    def median_bounds(K, j, ab):
        K1 = []
        K01 = []
        K0 = []
        for i in K:
            if ab[i] > ab[j]:
                K1.append(i)
            elif ab[i] == ab[j]:
                K01.append(i)
            else:
                K0.append(i)
        return K1, K01, K0

    def a__b__(K, a, b):
        a__ = 0
        b__ = 0
        for i in K:
            a__ += a[i]
            b__ += b[i]
        return a__, b__

    execute = True
    while execute and len(K) > 0:
        execute = False
        # passo 1
        logger.debug(f'passo1 K: {K}')
        j = median(K, ab)
        # passo 2
        logger.debug(f'passo2 j: {j}')
        K1, K01, K0 = median_bounds(K, j, ab)
        # passo 3
        logger.debug(f'passo3 K1: {K1} K01: {K01} k0: {K0}')
        a__, b__ = a__b__(K1 + K01, a, b)
        a__ += a_
        b__ += b_
        # passo 4
        logger.debug(f'passo4 a__: {a__} b__: {b__} a__/b__ {a__ / b__ } ab[j]: {ab[j]}')
        if len(K1) > 0 and a__ / b__ > ab[j]:
            K = K1
            execute = True
            continue
        # passo 5
        logger.debug(f'passo5 I1: {I1} K1: {K1} K01: {K01}')
        I1 = I1 + K1 + K01
        if len(K0) > 0:
            K0_max = 0
            for i in K0:
                if ab[i] > K0_max:
                    j = i
                    K0_max = ab[i]
            if ab[j] > a__ / b__:
                K = K0
                a_ = a__
                b_ = b__
                execute = True
                continue

        # if len(K) == 0:
        #     execute = False
    return I1
