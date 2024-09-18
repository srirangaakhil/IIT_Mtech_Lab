import itertools as it

def nList(L, N):
    return [list(it.islice(L, i, None, N)) for i in range(N)]
