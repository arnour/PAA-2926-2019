from paa191t1.pph.utils import select, median_of_medians, partition


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.r = a / b

    def __eq__(self, other):
        if other is not None and isinstance(other, Pair):
            return self.a == other.a and self.b == other.b
        return False

    def __gt__(self, other):
        if other is not None and isinstance(other, Pair):
            return self.r > other.r
        return False

    def __lt__(self, other):
        if other is not None and isinstance(other, Pair):
            return self.r < other.r
        return False

    def __str__(self):
        return f'([{self.a}, {self.b}], {self.r})'

    __repr__ = __str__

    def as_tuple(self):
        return (self.a, self.b, self.r)


class HiperbolicSet(object):

    def __init__(self, ra, rb):
        self.__ra = ra
        self.__rb = rb
        self.__values = []

    def add(self, t):
        self.__values.append(t)
        self.__ra += t.a
        self.__rb += t.b

    def add_all(self, ts):
        for t in ts:
            self.__values.append(t)
            self.__ra += t.a
            self.__rb += t.b

    def remove(self, index):
        t = self.__values.pop(index)
        self.__ra -= t.a
        self.__rb -= t.b

    def index(self, t):
        try:
            return self.__values.index(t)
        except ValueError:
            return -1

    def __str__(self):
        return f'R: {self.r} S: {self.__values}'

    @property
    def values(self):
        return self.__values.copy()

    @property
    def r(self):
        return self.__ra / self.__rb


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


def pph_n_lg_n(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    n.sort(key=lambda x: x.r, reverse=True)  # Utiliza TimSorte com complexidade n log n para ordenar os pares pela razao do maior para o menor
    i = 0
    while i < len(n):
        t = n[i]
        i += 1
        if t.r > s.r:
            s.add(t)
        else:
            i = len(n)
    return s


def pph_median(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    a = []
    b = []
    for t in n:
        a.append(t.a)
        b.append(t.b)
    k = list(range(len(n)))
    print(f'NNNNN {n}')
    print(f'KKKKKK {k}')
    nn = pph_med2(t0.a, t0.b, a, b, k)
    for i in nn:
        s.add(n[i])
    return s


def pph_m(n, t0):
    s = HiperbolicSet(t0.a, t0.b)
    for i, t in enumerate(n):   # O(n)
        if t.r < s.r:
            n.pop(i)
    continua = True

    while continua:
        continua = False
        median = median_of_medians(n, len(n) // 2)
        k1 = []
        k01 = []
        k0 = []
        for t in n:
            if t > median:
                k1.append(t)
            elif t < median:
                k0.append(t)
            else:
                k01.append(t)
        a_acum = t0.a + sum([t.a for t in k1]) + sum([t.a for t in k01])
        b_acum = t0.b + sum([t.b for t in k1]) + sum([t.b for t in k01])
        r_acum = (a_acum / b_acum)
        if r_acum > median.r:
            n = k1
            continua = True
            continue

        s.add_all(k1)
        s.add_all(k01)

        if len(k0) > 0:
            max_of_mins = max(k0)

            if max_of_mins.r > r_acum:
                n = k0
                s = HiperbolicSet(a_acum, b_acum)
                continua = True
                continue
    return s


def pph_med2(a0, b0, a, b, K):
    # passo 0
    I1 = []
    a_ = a0
    b_ = b0

    ab = [a[i] / b[i] for i in K]
    KK = []
    for k, i in enumerate(K):
        print(f'k,i :: ab[i] <= (a_ / b_) {k},{i} :: {ab[i]} -- {(a_ / b_)} ==> {ab[i] <= (a_ / b_)}')
        if ab[i] > (a_ / b_):
            KK.append(i)
    K = KK

    print(f'passo0: K : {K} // ab_ {ab} // {a0/b0}')

    def median(K, ab):
        print(f'K {K}, ab {ab}')
        abk = [ab[i] for i in K]
        m = select(abk.copy(), len(abk) // 2)
        print(f'm: {m}, ab: {ab}, ab.index == {ab.index(m)}')
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
        print(f'passo1 K: {K}')
        j = median(K, ab)
        # passo 2
        print(f'passo2 j: {j}')
        K1, K01, K0 = median_bounds(K, j, ab)
        # passo 3
        print(f'passo3 K1: {K1} K01: {K01} k0: {K0}')
        a__, b__ = a__b__(K1 + K01, a, b)
        a__ += a_
        b__ += b_
        # passo 4
        print(f'passo4 a__: {a__} b__: {b__} a__/b__ {a__ / b__ } ab[j]: {ab[j]}')
        if len(K1) > 0 and a__ / b__ > ab[j]:
            K = K1
            execute = True
            continue
        # passo 5
        print(f'passo5 I1: {I1} K1: {K1} K01: {K01}')
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
