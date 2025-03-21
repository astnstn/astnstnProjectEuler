import numpy as np
import time

start_time = time.time()


numbers = np.arange(1, 1000)

numbers_squared = numbers**2

a_b_square_sum_matrix = numbers_squared[:, None] + \
    numbers_squared[None, :]

# find the a, b sums which are found in numbers_squared
triplet_indices = np.argwhere(np.isin(a_b_square_sum_matrix, numbers_squared))

# a numbers which have square product
a_arr = numbers[triplet_indices[:, 0]]

# b numbers which have square product
b_arr = numbers[triplet_indices[:, 1]]


square_sum = a_arr**2 + b_arr**2

c_arr = np.sqrt(square_sum)

where_equal_1000 = (a_arr + b_arr + c_arr == 1000)
where_a_less_b_less_c = ((a_arr < b_arr) & (b_arr < c_arr))

where_found = where_equal_1000 & where_a_less_b_less_c

a, b, c = np.c_[a_arr, b_arr, c_arr][where_found][0]

duration = time.time() - start_time
print(f'found triplet ({a}, {b}, {c}) with product {a*b*c:.0f}')
print(f'compute time: {duration:.2f} seconds')
# zero seconds