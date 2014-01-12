#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 21 "Amicable numbers"
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2021
"""

import sys
import math

def get_pds(n): # pd: proper divisor
    pds = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            pds.append( i )
    return pds

def has_amicable_numer(n, pds_sums_dict):
    pds_sum = pds_sums_dict[n]
    if n == pds_sum:
        return False
    if pds_sum in pds_sums_dict and pds_sums_dict[pds_sum] == n:
        return True
    return False

def main():
    upper = 10000
    pds_sums_dict = {}
    for i in range(1, upper + 1):
        pds = get_pds(i)
        pds_sum = sum(pds)
        if pds_sum > upper:
            continue
        pds_sums_dict[i] = pds_sum

    amicable_numbers = []
    for n in pds_sums_dict.keys():
        if has_amicable_numer(n, pds_sums_dict):
            pds_sum = pds_sums_dict[n]
            amicable_numbers.append( (n, pds_sum) )
    print sum([pair[0] for pair in amicable_numbers])

if __name__ == '__main__':
    main()
