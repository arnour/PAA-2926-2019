
def get_r(s, a0, b0):
    sum_a = a0
    sum_b = b0
    for (a, b) in s:
        sum_a += a
        sum_b += b
    return sum_a/sum_b

def pph(n, a0=0, b0=0):
    s = []
    r = get_r(s, a0, b0)

    for (a, b) in n:
        if (a, b) not in s and get_r([], a, b) > r:
            s.append((a,b))
        elif (a, b) not in s and get_r([], a, b) < r:
            s.remove((a, b))
        r = get_r(s, a0, b0)
    return s, r