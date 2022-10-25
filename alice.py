#!/usr/bin/env python

from shift_ecb import *

import sys
import secrets
import logging

def main(args):
    if len(args) != 2:
        print("""\
        This script takes two plaintexts x0,x1 as arguments, 
        encrypts one of them chosen at random, and prints the ciphertext.
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
