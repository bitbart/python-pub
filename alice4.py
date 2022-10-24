#!/usr/bin/env python

import sys
import secrets
import random
import logging

def gen(n):
    k = []
    for i in range(n-1):
        k.append(secrets.choice([0,1]))
    l = 0
    for b in k:
        l = l ^ b
    k.append(l)
    return k

def enc(x,k):
    # print("x = " + x)
    # print("k = " + str(k))
    y = []
    for i in range(len(k)):
        y.append(chr(((ord(x[i])-ord('0'))^k[i])+ord('0')))
    y = ''.join(y)
    # print("y = " + y)
    return y

def main(args):
    logging.basicConfig(format='%(message)s', filename='alice3.log', level=logging.INFO)

    if len(args) != 2:
        print("""\
        This script encodes one of the two plaintexts given as arguments, 
        chosen at random, and prints the ciphertext.
        Usage: alice x0 x1
        """)
        sys.exit(0)

    assert (len(args[0])==len(args[1])), "Plaintexts with different lengths"
    for c in args[0]:
        assert(c in ['0','1'])
    for c in args[1]:
        assert(c in ['0','1'])

    logging.info("x0 = " + args[0])
    logging.info("x1 = " + args[1])

    k = gen(len(args[0]))
    logging.info("k = " + str(k))

    b = secrets.choice([0,1])
    logging.info("b = " + str(b))

    y = enc(args[b],k)
    logging.info("y = " + str(y))
    return (b,y)

if __name__ == '__main__':
    main(sys.argv[1:])
