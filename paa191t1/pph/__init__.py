class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.r = a / b

    def __eq__(self, other):
        if other is not None and isinstance(other, Pair):
            # return self.a == other.a and self.b == other.b
            return self.r == other.r
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

    def __getitem__(self, index):
        return self.__values[index]

    def __len__(self):
        return len(self.__values)

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
