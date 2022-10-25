#!/usr/bin/env python

from alice4 import *
from mallory4 import *
import sys
import logging

assert (len(sys.argv)==2 and int(sys.argv[1])>0),"Usage: privk-eav n_experiments"

logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)

S = 0                 # number of experiments where the adversary wins
N = int(sys.argv[1])  # total number of experiments

for i in range(N):
    logging.info("Experiment " + str(i+1))

    # M -> A : x0, x1
    (x0,x1) = plaintexts()
    logging.info("x0 = " + x0)
    logging.info("x1 = " + x1)
    
    # A -> M : y = Ek(x[b])
    (b,y) = main([x0,x1])
    logging.info("b = " + str(b))   
    logging.info("y = " + y)

    # M : bm   
    bm = guess(y)
    logging.info("bm = " + str(bm))
    
    if bm==b:
        logging.info("PrivK=1")
        S = S+1
    else:
        logging.info("PrivK=0")

print("Percentage of success: " + str(S*100./N))