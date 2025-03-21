def is_prime(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


limit = 2e6

current = 2
total_sum = 0

while current < limit:

    print(f'{100*current/limit:.2f}')
    if is_prime(current):
        total_sum += current

    current += 1


print(f'Total sum {total_sum}')
