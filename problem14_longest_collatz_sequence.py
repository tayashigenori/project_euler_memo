#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
Problem 15 "Longest Collatz sequence" �β�ˡ
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2014
"""

#collatz ���׻����롣
#���Ǥ˷׻��Ѥߤο��������Ĥ��ä������Ǥ���
def get_collatz_sequence(n, collatz_length_stored):
    """
    �㤨�� 13 ���鳫�Ϥ��� Collatz ��
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    ���֤���

    �⤷ 8 ���鳫�Ϥ��� Collatz �󤬤��Ǥ˷׻��Ѥߤʤ顢
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8,]
    �ޤǤ����׻����Ƥ�����֤���
    """
    collatz_sequence = [n,]
    while True:
        # check end
        if n == 1:
            break # ��λ

        # check already stored
        if n in collatz_length_stored:
            break # �Ǹ夬1�ǽ���äƤ��ʤ��ꥹ�Ȥ��֤�

        n = get_next_collatz(n)
        # ���������Ǥ��ɲ�
        collatz_sequence.append(n)
        #print collatz_sequence
    return collatz_sequence

def get_next_collatz(i):
    if i % 2 == 0:
        return i / 2
    return 3 * i + 1

def store_collatz_length(collatz_sequence, collatz_lengths):
    """
    ��: 13 ���鳫�Ϥ��� Collatz ��
    collatz_sequence = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    �Ȥ����ꥹ�Ȥ������ꡢ
    collatz_length = {
        13: 10, # [13, 40, 20, 10, 5, 16, 8, 4, 2, 1] ��Ĺ��
        40: 9,  #     [40, 20, 10, 5, 16, 8, 4, 2, 1] ��Ĺ��
        20: 8,  #         [20, 10, 5, 16, 8, 4, 2, 1] ��Ĺ��
        10: 7,  #             [10, 5, 16, 8, 4, 2, 1] ��Ĺ��
         5: 6,  #                 [5, 16, 8, 4, 2, 1] ��Ĺ��
        16: 5,  #                    [16, 8, 4, 2, 1] ��Ĺ��
         8: 4,  #                        [8, 4, 2, 1] ��Ĺ��
         4: 3,  #                           [4, 2, 1] ��Ĺ��
         2: 2,  #                              [2, 1] ��Ĺ��
         1: 1,  #                                 [1] ��Ĺ��
    }
    �Ȥ���������֤���
    """
    end_num = collatz_sequence[-1]
    while len(collatz_sequence) > 0:
        if end_num not in collatz_lengths:
            sys.stderr.write("There is something wrong in this algorithm. Can't compute collatz lengths.\n")
            sys.stderr.write("sequence: %s, collatz_lengths: %s\n" %(collatz_sequence, collatz_lengths))
            sys.exit(1)

        # ���Τ�Ĺ���ϡ�collatz_sequence = [13, 40, 20, 10, 5, 16, 8] ��Ĺ���פȡ�8 ���� 1 �ޤǤ�Ĺ�� (��¸�Ѥ�)�פ���
        # ����1���������� (8 ���������Ƥ���Τ�)
        this_collatz_length = len(collatz_sequence) + collatz_lengths[end_num] -1
        start_num = collatz_sequence[0]
        #print start_num, collatz_sequence
        if start_num not in collatz_lengths:
            collatz_lengths[start_num] = this_collatz_length
        else:
            # ���Ǥ˷׻��ѤߤʤΤǡ������礬̵�������������å�����
            # ���줬�Ǹ�����ǤΤϤ�
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

