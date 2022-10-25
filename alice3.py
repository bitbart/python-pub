#!/usr/bin/env python

import sys
import secrets
import logging

def gen():
    a = secrets.choice([0,1])
    k0 = secrets.randbelow(26)
    if a==0:
        k1=k0
    else:
        k1 = secrets.randbelow(26)
    return [k0,k1]

def enc(x,k):
    y0 = ''.join(map(chr, map(lambda n : ord('a')+(ord(n)-ord('a')+k[0])%26, x[0])))
    y1 = ''.join(map(chr, map(lambda n : ord('a')+(ord(n)-ord('a')+k[1])%26, x[1])))
    return y0+y1



def main(args):
    logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)
    
    if len(args) != 2:
        print("""\
        This script encodes one of the two plaintexts given as arguments, 
        chosen at random, and prints the ciphertext.
        Usage: alice x0 x1
        """)
        sys.exit(0)

    k = gen()
    logging.info("k = " + str(k))
    
    b = secrets.choice([0,1])

    y = enc(args[b],k)

    return (b,y)
    
if __name__ == '__main__':
    main(sys.argv[1:])
