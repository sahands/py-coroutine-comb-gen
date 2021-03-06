from combgen.helpers.permutations import transpose


def gen_all(n):
    # Pad on both sides to allow for a natural stop
    pi = [n + 1] + list(range(1, n + 1)) + [n + 1]
    inv = pi[:]
    # Keep track of directions, all starting negative (move left)
    d = [-1] * (n + 2)
    x = n  # x is the active element
    yield pi[1:-1]
    while x > 0:
        y = pi[inv[x] + d[x]]  # y is the element next to x in direction d[x]
        if x < y:
            d[x] = -d[x]  # Switch direction
            x -= 1  # Change active element to x - 1
        else:
            transpose(pi, inv, x, y)
            yield pi[1:-1]  # New permutation is generated
            x = n  # Change active element to n
