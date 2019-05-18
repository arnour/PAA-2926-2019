class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.r = a / b

    def __eq__(self, other):
        if other is not None and isinstance(other, Pair):
            return self.a == other.a and self.b == other.b
        return False

    def __str__(self):
        return f'({self.a}, {self.b}, {self.r})'

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
        elif index > -1 and t.r < s.r:
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
        if t.r >= s.r:
            s.add(t)
        else:
            i = len(n)
    return s
