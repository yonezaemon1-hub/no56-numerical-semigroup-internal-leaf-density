#!/usr/bin/env python3
"""Proves the decimal inequalities from Q32 by exact rational arithmetic.
It verifies arithmetic and a stated recurrence count, NOT Q32 independently.
"""
from fractions import Fraction

q = Fraction(543583947, 3758096384)
prod = Fraction(1, 1)
for k in range(33, 71):
    t = (k-1)//2 - 3
    u = Fraction(1, 2) * Fraction(3, 4)**t
    assert 0 < u < 1
    prod *= 1-u
tail_union_bound = 4 * Fraction(3, 4)**32
assert 0 < tail_union_bound < 1
lower = q*prod*(1-tail_union_bound)
assert lower > Fraction(1314883, 10000000)
assert q < Fraction(1446435, 10000000)
print('PASS exact rational bound: 0.1314883 < c < 0.1446435')
print('VERIFIED arithmetic only: Q32 recurrence count independently checked in C++ source')
