#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 21 "Lexicographic permutations"
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2024
"""

"""
方針：ユークリッドの互除法の応用

(1) 上から1桁目を求める

 (1A) 除算
 1桁目が "0", "1", ... の順列はおのおの 9! 個あるので、
 100万 / 9! = 2 より

 * 1桁目が "0" の順列
 * 1桁目が "1" の順列
 には 100万番目は含まれず、
 100万番目は、1桁目が "2" である。

 (1B) 余りの計算
 100万 - 9! * 2 = 274240
 100万番目は、1桁目が "2" のもののうち、
 274240 番目である

(2) 上から2桁目を求める

二桁目は、上記の計算を
* 100万 <-- 274240
* 9! <-- 8!
と代入しなおして計算すればよい

 (2A) 除算
 1桁目が "2" かつ 2桁目が "0", "1", ... の順列はおのおの 8! 個あるので、
 274240 / 8! = 6 より、
 2桁目は、7 であることが分かる

 ※1桁目に "2" かもう使用されているので
   小さいほうから数えて "0", "1", "3", "4", "5", "6" がこの商「6」に該当する

 (2B) 余りの計算... 274240 % 8!
 274240 % 8! = 32320
 より、100万番目は、"27" で始まるもののうち、32320番目

... 以下これを繰り返していく
"""

import sys
import math

def perm(target = 999999, keta_suu = 10):
    answer = ""
    tmp_answers = {} # 商をメモしておくリスト

    for keta in range(1, keta_suu + 1):# 上から keta (= 1 ~ 10) 桁目について
        fact = math.factorial(keta_suu - keta)

        quot = target / fact
        rem = target % fact
        tmp_answers[keta] = quot # 商をメモ
        target = rem

    available_numbers = range(keta_suu)# 0 ~ 9
    for keta, quot in tmp_answers.items():
        # 0~9 のうち、quot 番目に小さいものがこの桁の数字
        digit = available_numbers.pop(quot) # 一回使ったものはもう使えないので pop する
        answer += str(digit)
    return answer

def main():
    # このアルゴリズムだと小さいものから 0 番目から始まるので、99万9999番目を求める
    print perm(999999, 10)

if __name__ == '__main__':
    main()
