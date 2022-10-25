#!/usr/bin/env python

from shift_unbal import *

import sys
import secrets
import logging

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
