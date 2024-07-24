from copy import deepcopy


def find_missing_bf(A, B, N, M):
    copyA = deepcopy(A)
    for i in B:
        for j in A:
            if i == j and i in copyA:
                copyA.remove(i)
    return copyA


def find_missing_optimized(A, B, N, M):
    B = set(B)
    return [j for j in A if j not in B]
