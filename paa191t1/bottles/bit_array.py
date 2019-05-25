from bitarray import bitarray


class BitArray(bitarray):
    def __lshift__(self, count):
        if count > 0:
            return self[count:] + type(self)('0') * count
        else:
            return self

    def __rshift__(self, count):
        if count > 0:
            return type(self)('0') * count + self[:-count]
        else:
            return self

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, self.to01())
