

def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


search_number = 10001

current_number = 2
prime_count = 0

while True:

    if is_prime(current_number):
        prime_count += 1

    if prime_count == search_number:
        break

    current_number += 1

print(f'prime number {prime_count} is {current_number}')
