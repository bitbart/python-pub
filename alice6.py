#!/usr/bin/env python

# Quasi-OTP with plaintexts of arbitrary length: gen(n) never produces a key of n 0s

import sys
import secrets
import logging
from functools import reduce

def gen(n):
    found = False
    while not found:
        k = []
        for i in range(n):
            k.append(secrets.choice([0,1]))
        for bi in k:
            if bi==1:
                found=True
    return k

def enc(x,k):
    y = []
    for i in range(len(k)):
        y.append(str(int(x[i]) ^ k[i]))
    y = ''.join(y)
    return y

def main(args):
    logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)
    
    if len(args) != 2:
        print("""\
        This script encodes one of the two plaintexts given as arguments, 
        chosen at random, and prints the ciphertext.
        Usage: alice x0 x1
        """)
        sys.exit(0)

    assert (len(args[0])==len(args[1])), "Plaintexts of different lengths"
    assert (reduce(lambda x, y: x and y in ['0','1'], args[0],True)), "Plaintext x0 not bitstring"
    assert (reduce(lambda x, y: x and y in ['0','1'], args[1],True)), "Plaintext x1 not bitstring"
    
    k = gen(len(args[0]))
    logging.info("k = " + ''.join(map(lambda b : str(b),k)))
    
    b = secrets.choice([0,1])

    y = enc(args[b],k)

    return (b,y)
    
if __name__ == '__main__':
    main(sys.argv[1:])
