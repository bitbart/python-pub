#!/usr/bin/env python

import alice2
import logging
import random

logging.basicConfig(format='%(message)s', filename='alice2.log', level=logging.INFO)
N = 10000   # number of experiments
S = 0   # number of success

for i in range(N):
    logging.info("Experiment " + str(i+1))
    (b,y) = alice2.main('a b'.split(' '))

    if y=='z':
        bm = 0
    else:
        bm = 1

    if bm==b:
        logging.info("PrivK=1")
        S = S+1
    else:
        logging.info("PrivK=0")

print("Percentage of success: " + str(S*100./N))
