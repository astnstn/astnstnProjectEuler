# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:41:53 2025

@author: AustenStone
"""
import time

start = time.time()


def divisible(n):
    for factor in factors[::-1]:
        if n % factor != 0:
            return False
    return True


# no imports
number = 2520

factors = list(range(1, 21))


while True:
    if divisible(number):
        break

    number += 1

duration = time.time() - start
# %%

print(f'answer: {number}, duration: {duration:.2f} seconds')
# about 50 seconds