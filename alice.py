#!/usr/bin/env python

import sys
import secrets
import logging

def gen():
    k = secrets.randbelow(26)
    return k

def enc(x,k):
    return  ''.join(map(chr, map(lambda n : ord('a')+(ord(n)-ord('a')+k)%26, x)))

def dec(y,k):
    return  ''.join(map(chr, map(lambda n : ord('a')+(ord(n)-ord('a')-k)%26, y)))

def main(args):
    logging.basicConfig(format='%(message)s', filename='alice.log', level=logging.INFO)
    
    if len(args) != 2:
        print("""\
        This script encodes one of the two plaintexts given as arguments, 
        chosen at random, and prints the ciphertext.
        Usage: alice x0 x1
        """)
        sys.exit(0)

    logging.info("x0 = " + args[0])
    logging.info("x1 = " + args[1])

    k = gen()
    logging.info("k = " + str(k))
    
    b = secrets.choice([0,1])
    logging.info("b = " + str(b))

    y = enc(args[b],k)
    logging.info("y = " + y)

    print(y)
    print(dec(y,k))
    
    return (b,y)
    
if __name__ == '__main__':
    main(sys.argv[1:])
