#!/usr/bin/env python

import sys
import logging

from cipher import *
from mallory0 import *

# Adv: Mallory1
P = ShiftECB()

# Adv: Mallory2
# P = Shift1Unbal()

# Adv: Mallory3
# P = Vigenere2Unbal()

# Adv = Mallory4
# P = OTPlastXor(3)

# Adv: Mallory5
# P = TwoTP(4)

# Adv: Mallory6
# P = QuasiOTP(4)

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
    (b,y) = P.exp(x0,x1)
    logging.info("b = " + str(b))   
    logging.info("y = " + y)

    # M : bm   
    bm = guess(y)
    logging.info("bm = " + str(bm))
    
    if bm==b:
        logging.info("PrivK = 1 (Mallory wins)")
        S = S+1
    else:
        logging.info("PrivK = 0 (Mallory loses)")

print("Percentage of success: " + str(S*100./N))
