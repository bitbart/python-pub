#!/usr/bin/env python

def plaintexts():
    return ("00000","11111")

def guess(y):
    allZ = True          # allZ=True iff all bits in ciphertext are 0
    for yi in y:
        if int(yi)==1:
            allZ = False
            
    if allZ:
        bm = 1
    else:
        bm = 0
    return bm
