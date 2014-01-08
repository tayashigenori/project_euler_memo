#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 15 "Lattice Paths" の解法
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2015
"""

import sys

#n行 m列の格子の、左上から右下へ至る経路の個数を数える関数
def count_lattice_paths(n = 2, m = 2):
    """
    2*3 の場合、
    lattice = [
        [1,1,1,1], // 0行目
        [1,2,3,4], // 1行目
        [1,3,6,10] // 2行目
    ]
    を返す
    """
    lattice = initialize_lattice(n, m)
    lattice = increment_lattice(n, m, lattice)
    return lattice[n][m]

def initialize_lattice(n, m):
    """
    2*3 の場合、
    lattice = [
        [1,1,1,1], // 0行目
        [1,], // 1行目
        [1,] // 2行目
    ]
    を返す
    """
    # 0行目を 1 で初期化
    lattice = []
    zeroth_row = [1,] * (m+1) # [1,1,...]
    lattice.append( zeroth_row )
    # 各行の0列目を 1 で初期化
    for i in range(1, n+1): # i行目
        ith_row = [1,]
        lattice.append(ith_row)
    return lattice
def increment_lattice(n, m, lattice):
    for j in range(1, m+1): # j列目の
        for i in range(1, n+1): # i行目
            #print grid
            try:
                # lattice[i][j] を追加
                lattice[i].append( lattice[i-1][j] + lattice[i][j-1] )
            except IndexError:
                sys.stderr.write("There is something wrong in this algorithm!\n")
                sys.stderr.write("Out of index: n:%d, m:%d\n" %(n,m))
                sys.exit(1)
    return lattice

def main():
    test = count_lattice_paths(2,2)
    if test != 6:
        sys.stderr.write("There is something wrong in this algorithm!\n")
        sys.exit(1)

    answer = count_lattice_paths(20,20)
    sys.stdout.write("%s\n" %answer)

if __name__ == '__main__':
    main()
