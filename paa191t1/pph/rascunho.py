
def get_r(s, a0, b0):
    sum_a = a0
    sum_b = b0
    for (a, b) in s:
        sum_a += a
        sum_b += b
    return sum_a / sum_b


def pph(n, a0, b0):
    s = []
    r = get_r(s, a0, b0)

    print(a0, b0, s, r)
    changed = True
    while changed:  
        changed = False      
        for (a, b) in n:
            curr_r = get_r([], a, b)
            if (a, b) not in s and curr_r > r:
                s.append((a, b))
                changed = True
            elif (a, b) in s and curr_r < r:
                s.remove((a, b))
                changed = True
            if changed:
                r = get_r(s, a0, b0)
                print("s:", s, "rmax:", r, "a:", a, "b:", b, "r:", curr_r)
                break        
    return a0, b0, s, r

n = [
    (2, 5),
    (1, 3),
    (3, 8),
    (6, 6),
    (5, 16)
]

print(pph(n, 2, 17))
print(n)