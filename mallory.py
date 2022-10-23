#!/usr/bin/env python

import alice
import logging

logging.basicConfig(format='%(message)s', filename='alice.log', level=logging.INFO)
N = 100   # number of experiments
S = 0   # number of success

for i in range(N):
    logging.info("Experiment " + str(i+1))
    (b,y) = alice.main('aa ab'.split(' '))

    if y[0]==y[1]:
        bm = 0
    else:
        bm = 1

    if bm==b:
        logging.info("PrivK=1")
        S = S+1
    else:
        logging.info("PrivK=0")

print("Percentage of success: " + str(S*100./N))
