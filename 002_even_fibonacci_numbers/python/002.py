# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 11:35:57 2025

@author: AustenStone
"""


sequence = [1, 2]
even_sum = 2

while sequence[-1] < 4e6:
    
    next_term = sequence[-2] + sequence[-1]
    
    if next_term % 2 == 0:
        even_sum += next_term
        
    sequence += [next_term]
    
    