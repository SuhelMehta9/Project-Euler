# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

usr_input = int(input('Enter the number: '))
sum_of_squares = (usr_input * (usr_input + 1) * (2*usr_input + 1)) / 6 # This is the formula 
# to find sum of squares of numbers

square_of_sum = usr_input*(usr_input+1)/2 # To sum all numbers between 1 and usr_input
square_of_sum = square_of_sum**2 # Square of sum
print(square_of_sum-sum_of_squares)
