numbers = list(range(1, 101))

squares = list(map(lambda x: x**2, numbers))

sum_of_squares = sum(squares)
square_of_sum = sum(numbers)**2

difference = square_of_sum - sum_of_squares
