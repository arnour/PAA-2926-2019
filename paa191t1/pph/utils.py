def median_of_medians(A, i):

    # divide A into sublists of len 5
    sublists = [A[j:j + 5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        # the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians) // 2)

    # partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i - k - 1)
    else:  # pivot = k
        return pivot


def median_of_medians2(A, i):

    # divide A into sublists of len 5
    sublists = [A[j:j + 5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        # the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians) // 2)
    print(f'medians {medians} index: {len(medians) // 2}')
    # partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i - k - 1)
    else:  # pivot = k
        return pivot


def partition(pivot, n):
    left = []
    right = []
    for i in n:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
    return left, right


def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex + 5 < len(L) - 1:
        S.append(L[lIndex:lIndex + 5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList) - 1) / 2)))
    med = select(Meds, int((len(Meds) - 1) / 2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j - len(L1) - len(L2))
