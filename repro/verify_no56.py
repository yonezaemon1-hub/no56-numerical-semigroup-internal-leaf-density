#!/usr/bin/env python3
"""No.56 internal audit, stdlib-only Python 3.10+.
Independently constructs semigroups as explicit membership sets, then counts
incremental local events. It does NOT claim to audit the general proof.
"""
from itertools import product

EXPECTED = {
    6: (28, 7), 7: (56, 13), 8: (112, 19), 9: (224, 41),
    10: (448, 73), 11: (896, 152), 12: (1792, 284),
    13: (3584, 578), 14: (7168, 1104), 15: (14336, 2245),
}
EXPECTED_Q = {6: 13, 12: 596, 18: 34870, 22: 543345}


def count_direct(m):
    f = 2*m + 3
    n = 0
    leaves = 0
    for a1, a2 in ((0, 0), (1, 0), (0, 1)):
        for b1, b2 in product((0, 1), repeat=2):
            if a1 and not (b1 and b2):
                continue
            if a2 and not b2:
                continue
            for free in product((0, 1), repeat=m-4):
                s = {0, m, 2*m} | set(range(f+1, f+m+1))
                if a1: s.add(m+1)
                if a2: s.add(m+2)
                if b1: s.add(2*m+1)
                if b2: s.add(2*m+2)
                s.update(m+i for i, val in enumerate(free, 4) if val)
                # The set's tail above F is implicitly all present.
                def is_member(z):
                    return (z in s) or z > f
                for i in range(m, f+1):
                    if not is_member(i):
                        continue
                    for j in range(m, f+1-i):
                        if is_member(j):
                            assert is_member(i+j), (m, i, j)
                n += 1
                if all(any(is_member(i) and is_member(x-i)
                           for i in range(m, x//2+1))
                       for x in range(f+1, f+m+1)):
                    leaves += 1
    return n, leaves


def count_prefix(r):
    """Unweighted prefixes; initial-case weights 4:1:2 are applied at end."""
    def visit(k, selected):
        if k > r:
            return 1
        exists_old_pair = any(i in selected and k-i in selected
                              for i in range(1, k//2+1))
        with_k = visit(k+1, selected | {k})
        without_k = visit(k+1, selected) if exists_old_pair else 0
        return with_k + without_k
    return (4*visit(4, frozenset()) +
            visit(4, frozenset((1,))) +
            2*visit(4, frozenset((2,))))


def main():
    for m, expected in EXPECTED.items():
        got = count_direct(m)
        assert got == expected, (m, got, expected)
        assert got[0] == 7*2**(m-4)
        print('PASS m={}: N={} I={} L={}'.format(m, got[0], got[0]-got[1], got[1]))
    for r, expected in EXPECTED_Q.items():
        got = count_prefix(r)
        assert got == expected, (r, got, expected)
        print('PASS Q_{}={}/{}'.format(r, got, 7*2**(r-3)))
    print('PASS internal Python checks; Windows execution still needs a user-generated log.')

if __name__ == '__main__':
    main()
