# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:41:53 2025

@author: AustenStone
"""
import time
import numpy as np

start_time = time.time()

###

stride = 0.5e6

start = 1

factors = np.arange(1, 21)

while True:

    test_numbers = np.arange(start, start + stride, dtype='int')

    remainders = test_numbers[:, None] % factors[None, :]

    remainders = np.sum(remainders, axis=-1)

    where_zero_remainders = np.argwhere(remainders == 0)
    if where_zero_remainders.size > 0:
        solution = test_numbers[where_zero_remainders[0]]
        print(solution)
        break

    start = test_numbers[-1] + 1


duration = time.time() - start_time

print(f'answer: {solution}, duration: {duration:.2f} seconds')
# about 15 seconds
