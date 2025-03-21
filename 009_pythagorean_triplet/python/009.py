import time

start_time = time.time()

found = False
for a in range(1, 1000):

    print(f'{a*100/1000:.2f}%')

    for b in range(a, 1000):

        for c in range(b, 1000):

            if a**2 + b**2 == c**2:
                if a + b + c == 1000:

                    found = True
                    break

        if found == True:
            break

    if found == True:
        break

print(f'triplet found ({a}, {b}, {c}) with product {a*b*c}')

duration = time.time() - start_time

print(f'compute time: {duration:.2f} seconds')
# took about 13 seconds