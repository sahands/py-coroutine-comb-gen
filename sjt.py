from __future__ import print_function
from time import sleep
from nobody import nobody

__author__ = "Sahand Saba"


def sjt(pi, inv, i, coroutines):
    d = -1
    while True:
        j = inv[i]
        if pi[j] < pi[j + d]:
            d = -d
            yield next(coroutines[i - 1])
        else:
            pi[j], pi[j + d] = pi[j + d], pi[j]
            inv[i] += d
            inv[pi[j]] -= d
            yield True


def setup(n):
    # Start with the identity permutation
    pi = list(range(1, n + 1))

    # Pad pi with n + 2 on both sides, so
    # that pi[i] will always be < the two ends.
    pi = [n + 2] + pi + [n + 2]
    inv = pi[:-1]

    coroutines = [nobody()]
    coroutines.extend(
            sjt(pi, inv, i, coroutines)
            for i in range(1, n + 1)
            )
    coroutines += [nobody()]

    # The lead coroutine will be the
    # item n in the permutation
    lead_coroutine = coroutines[-2]
    return pi, lead_coroutine


def permutations(n):
    pi, lead_coroutine = setup(n)
    yield pi[1:-1]
    while next(lead_coroutine):
        yield pi[1:-1]


def cyclic_test(n):
    pi, lead_coroutine = setup(n)
    c = 0
    while True:
        print(''.join(str(x) for x in pi[1:-1]))
        c += 1
        if not next(lead_coroutine):
            print('-------')
            print(c)
            print('-------')
            sleep(1)
            c = 0


if __name__ == '__main__':
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(1)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(2)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(3)))
    print('\n'.join(''.join(str(x) for x in pi) for pi in permutations(4)))
    cyclic_test(3)
