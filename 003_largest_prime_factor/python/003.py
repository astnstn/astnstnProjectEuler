# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:46:05 2025

@author: AustenStone
"""
import time

start = time.time()

def check_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True



number = 600851475143

current = int(number**0.5) + 1

prime_found = False

while not prime_found:

    if check_prime(current):
        if number % current == 0:
            prime_found = True
            print(current)
            break

    current -= 1


duration = time.time() - start

print(f'answer: {current} found in {duration:.3f} seconds')

# took about 1.8 - 2.1 seconds