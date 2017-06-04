#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: nsum.py
module description: implement for nsum using memoization
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/31 21:41
"""
known_sum = {0: 0}

def nsum(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n-1)
    known_sum[n] = res
    return res

