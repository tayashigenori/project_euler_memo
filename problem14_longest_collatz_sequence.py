#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
Problem 15 "Longest Collatz sequence" の解法
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2014
"""

#collatz 列を計算する。
#すでに計算済みの数字が見つかった時点でやめる
def get_collatz_sequence(n, collatz_length_stored):
    """
    例えば 13 から開始した Collatz 列
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    を返す。

    もし 8 から開始する Collatz 列がすでに計算済みなら、
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8,]
    までだけ計算してこれを返す。
    """
    collatz_sequence = [n,]
    while True:
        # check end
        if n == 1:
            break # 完了

        # check already stored
        if n in collatz_length_stored:
            break # 最後が1で終わっていないリストを返す

        n = get_next_collatz(n)
        # 末尾に要素を追加
        collatz_sequence.append(n)
        #print collatz_sequence
    return collatz_sequence

def get_next_collatz(i):
    if i % 2 == 0:
        return i / 2
    return 3 * i + 1

def store_collatz_length(collatz_sequence, collatz_lengths):
    """
    例: 13 から開始した Collatz 列
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    というリストを受け取り、
    collatz_length = {
        13: 10, # [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] の長さ
        40: 9,  #     [40, 20, 10, 5, 16, 8, 4, 2, 1] の長さ
        20: 8,  #         [20, 10, 5, 16, 8, 4, 2, 1] の長さ
        10: 7,  #             [10, 5, 16, 8, 4, 2, 1] の長さ
         5: 6,  #                 [5, 16, 8, 4, 2, 1] の長さ
        16: 5,  #                    [16, 8, 4, 2, 1] の長さ
         8: 4,  #                        [8, 4, 2, 1] の長さ
         4: 3,  #                           [4, 2, 1] の長さ
         2: 2,  #                              [2, 1] の長さ
         1: 1,  #                                 [1] の長さ
    }
    という辞書を返す。
    """
    end_num = collatz_sequence[-1]
    while len(collatz_sequence) > 0:
        if end_num not in collatz_lengths:
            sys.stderr.write("There is something wrong in this algorithm. Can't compute collatz lengths.\n")
            sys.stderr.write("sequence: %s, collatz_lengths: %s\n" %(collatz_sequence, collatz_lengths))
            sys.exit(1)

        # 全体の長さは「collatz_sequence = [13, 40, 20, 10, 5, 16, 8] の長さ」と「8 から 1 までの長さ (保存済み)」の和
        # から1を引いたもの (8 を二回数えているので)
        this_collatz_length = len(collatz_sequence) + collatz_lengths[end_num] -1
        start_num = collatz_sequence[0]
        #print start_num, collatz_sequence
        if start_num not in collatz_lengths:
            collatz_lengths[start_num] = this_collatz_length
        else:
            # すでに計算済みなので、不整合が無いかだけチェックする
            # これが最後の要素のはず
            if collatz_lengths[start_num] != this_collatz_length:
                sys.stderr.write("There is something wrong in this algorithm.\n")
                sys.stderr.write("sequence: %s, lengths: %s, this length (unmatched): %s\n" %(collatz_sequence, collatz_lengths, this_collatz_length))
                sys.exit(1)

        collatz_sequence.pop(0)

    return collatz_lengths

def main():
    max = 1000000 # one million
    collatz_lengths_stored = {1:1}

    for i in range(1, max + 1):
        collatz_sequence = get_collatz_sequence(i, collatz_lengths_stored)
        collatz_lengths_stored = store_collatz_length(collatz_sequence, collatz_lengths_stored)

    for start_num,collatz_length in sorted(collatz_lengths_stored.items(), key=lambda x:x[1]):
        sys.stdout.write("start number: %s, collatz sequence length: %s\n" %(start_num, collatz_length))

if __name__ == '__main__':
    main()

