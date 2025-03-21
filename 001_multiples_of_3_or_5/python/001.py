# Find the sum of all the multiples of 3 or 5 below 1000
import time 

start = time.time()
multiples = []

for i in range(1000):

    if i % 3 == 0:
        multiples.append(i)
    elif i % 5 == 0:
        multiples.append(i)
        

duration = time.time() - start        
print(f'Answer: {sum(multiples)} calculated in {duration:.3f} seconds')
