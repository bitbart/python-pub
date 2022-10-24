#!/usr/bin/env python

import alice4
import logging
import random

logging.basicConfig(format='%(message)s', filename='alice4.log', level=logging.INFO)
N = 1000   # number of experiments
S = 0   # number of success

for i in range(N):
    logging.info("Experiment " + str(i+1))
    x0 = "000"
    x1 = "001"
    (b,y) = alice4.main([x0,x1])

    n = 0
    for bi in y[:-1]:
        n = n ^ int(bi)

    if n==int(y[2]):
        bm = 0
    else:
        bm = 1

    if bm==b:
        logging.info("PrivK=1")
        S = S+1
    else:
        logging.info("PrivK=0")

print("Percentage of success: " + str(S*100./N))
