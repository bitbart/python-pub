#!/usr/bin/env python

# Two-time pad with plaintexts of length 2*N

import sys
import secrets
import logging

N = 2

def gen():
    k = []
    for i in range(N):
        k.append(secrets.choice([0,1]))
    k = k + k
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

    assert (len(args[0])==2*N and len(args[1])==2*N), "Plaintexts of wrong length"
    for c in args[0]:
        assert(c in ['0','1'])
    for c in args[1]:
        assert(c in ['0','1'])

    k = gen()
    logging.info("k = " + str(k))
    
    b = secrets.choice([0,1])

    y = enc(args[b],k)

    return (b,y)
    
if __name__ == '__main__':
    main(sys.argv[1:])
