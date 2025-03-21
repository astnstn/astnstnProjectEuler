

def is_even(n):
    return True if n % 2 == 0 else False


def collatz(n):
    return n//2 if is_even(n) else 3*n + 1


def collatz_length(start_number):

    current = start_number
    step_count = 1

    while True:

        current = collatz(current)
        step_count += 1

        if current == 1:
            break

    return step_count


starting_numbers = range(1, int(1e6))

longest_chain = 1
best_starting_number = 1


for number in starting_numbers:
    
    print(number)
    
    length = collatz_length(number)
    
    if length > longest_chain:
        longest_chain = length
        best_starting_number = number


print(f'starting number: {best_starting_number}')