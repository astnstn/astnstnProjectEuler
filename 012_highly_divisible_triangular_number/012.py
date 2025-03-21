# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:11:54 2025

@author: AustenStone
"""


def find_factors(n):

    factors = []

    for i in range(1, int(n**0.5) + 1):

        if n % i == 0:

            factors.append(i)
            factors.append(n//i)

    factors = sorted(list(set(factors)))
    return factors


current_number = 1
total_sum = 0

while True:

    total_sum += current_number

    factors = find_factors(total_sum)
    num_factors = len(factors)
    print(f'{total_sum}: {num_factors}')

    if num_factors > 500:
        break

    current_number += 1
