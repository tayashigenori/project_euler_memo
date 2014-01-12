#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem 22 "Names scores"
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%2022
"""

import sys

def get_list(filename = "./names.txt"):
    res = []
    f = open(filename)
    try:
        for line in f.readlines():
            line = line.strip()
            res += line.split(",")
    finally:
        f.close()
    # remove double quotation
    return [r[1:-1] for r in res]

def get_name_scores(sorted_names):
    res = []
    for name in sorted_names:
        res.append( get_name_score(name, sorted_names) )
    return res
def get_name_score(name, sorted_names):
    return get_alphabetical_position(name, sorted_names) * get_alphabetical_value(name)

def get_alphabetical_position(name, sorted_names):
    return sorted_names.index(name) + 1
def get_alphabetical_value(name):
    alphabets = [chr(i) for i in range(65, 91)]
    value = 0
    for c in name:
        if c not in alphabets:
            raise Exception("invalid name: %s" %name)
        value += ord(c) - 64
    return value

def main():
    names = get_list()
    names.sort()
    scores = get_name_scores(names)
    print sum(scores)

if __name__ == '__main__':
    main()
