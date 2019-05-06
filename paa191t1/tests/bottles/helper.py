def b(i, n, k, x, t=0):
    if k > 0:
        step = round(((n - i)**(k - 1))**(1 / k))
        lower = i
        for _ in range(int(n / step) + 1):
            upper = min(step + lower, n)
            print('[{}, {}]({})'.format(lower, upper, step))
            if (step > 1) and (x <= upper):
                b(lower, upper, k - 1, x, t + 1)
                break
            elif (step == 1) and (x == upper or upper - 1 == x):
                b(lower, upper, k - 1, x, t + 1)
                break
            else:
                lower = upper
                t += 1
    else:
        print('>>> i={}, n={}, k={}, t={}, x={}'.format(i, n, k, t, x))


if __name__ == "__main__":
    i = 0
    n = 100
    k = 4
    x = 100
    print('max= ', round(k * (n**(1 / k))))
    b(i, n, k, x)
