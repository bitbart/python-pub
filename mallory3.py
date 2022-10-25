#!/usr/bin/env python

def plaintexts():
    return ("aa","ab")

def guess(y):
    if y[0]==y[1]:
        bm = 0
    else:
        bm = 1
    return bm
